# This will absctract the socket communication to a simple moduel that can be called and used to setup the server
import socket
from threading import Thread
import classes.queue
import json

def read_header(byte_string, protocol_size=1,bytes_size=7):
    protocol        = byte_string[:protocol_size]
    size            = byte_string[-bytes_size:]
    protocol        = int.from_bytes(protocol,"big")
    size            = int.from_bytes(size,"big")
    return          protocol, size

def make_header(protocol, data_size, protocol_size=1, bytes_size=7):
    protocol_bytes  = int.to_bytes(protocol,protocol_size,"big")
    size_bytes      = int.to_bytes(data_size,bytes_size,"big")
    return protocol_bytes + size_bytes

class Connection(Thread):
    def __init__(self, server_address, server_port):
        Thread.__init__(self)
        self.deamon=True

        self.server_address = server_address
        self.server_port = server_port
        self.recv_que = classes.queue.Queue()
        self.send_que = classes.queue.Queue()

        self.send = self.send_que.enqueue
        self.recv = self.recv_que.dequeue

        self.halt = False
        self.error = ""
        self.started = False

        self.start()

    def run(self):
        try:
            self.connected = False
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.server_address, self.server_port))
            self.recv_loop = Recv_loop(self.socket, self.recv_que, self)
            self.send_loop = Send_loop(self.socket, self.send_que)
        except Exception as e:
            self.halt = True
            self.error = e
        self.started = True
        

    def kill(self):
        self.recv_loop.alive = False
        self.send_loop.alive = False
        self.socket.shutdown(2) # socket.SHUT_RDWR (Evaluated to save an import)


# Thread code to handle loop recv
class Recv_loop(Thread):
    def __init__(self, socket, queue, parent, header_size=8, max_buffer = 4096):
        Thread.__init__(self)
        self.deamon     = True
        self.parent     = parent
        self.alive      = True
        self.socket     = socket
        self.queue      = queue
        self.header_size= header_size
        self.max_buffer = max_buffer

        self.start()
    
    def run(self):
        while self.alive:
            header = self.socket.recv(self.header_size)
            if header == b"":
                # Socket dead as it is receiving nothing
                self.parent.kill()
            protocol, data_size = read_header(header)

            data = b""
            # Read large data off in chunks of max buffer read size
            while data_size >= self.max_buffer:
                data += self.socket.recv(self.max_buffer)
                data_size -= self.max_buffer
            
            # Read any remaning data if any.
            data_size = reversed(bin(data_size)[2:])
            for i, num in enumerate(data_size):
                if num == "1":
                    data += self.socket.recv(2**(i))

            # Make Dict
            if protocol >= 200:
                # Protocol in Fx block, use raw bytes for data
                item = {"ID":protocol,"DATA":data}
            else:            
                # Protocol out of the Fx block, JSON decode byte string
                item = {"ID":protocol,"DATA":json.loads(data.decode("utf-8"))}            
            
            self.queue.enqueue(item)


# Thread code to handle loop send
class Send_loop(Thread):
    def __init__(self, socket, queue):
        Thread.__init__(self)
        self.deamon=True

        self.alive = True
        self.socket = socket
        self.queue = queue

        self.start()
    
    def run(self):
        while self.alive:
            if self.queue.isdata():
                data = self.queue.dequeue()

                # ID is above 200 so the data should already be bytes
                if data["ID"] >= 200:
                    data_bytes = data["DATA"]
                else:
                    data_bytes = json.dumps(data["DATA"]).encode("utf-8")
                header = make_header(data["ID"], len(data_bytes))
                self.socket.send(header)
                self.socket.send(data_bytes)