# This will absctract the socket communication to a simple moduel that can be called and used to setup the server
import socket
from threading import Thread
import classes.queue
import json

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
    def __init__(self, socket, queue, parent, buffer_size=4096):
        Thread.__init__(self)
        self.deamon=True
        self.parent = parent
        self.alive = True
        self.socket = socket
        self.queue = queue
        self.buffer_size=buffer_size

        self.start()
    
    def run(self):
        while self.alive:
            data = self.socket.recv(self.buffer_size)
            if data == b"":
                # Socket dead as it is receiving nothing
                self.parent.kill()
            data = data.decode("utf-8")
            # Malformed JSON object. Extra depth and comma at end.
            # eg "data 1","data 2",
            # Remove end comma and put in [] then hand to json to unpack
            data = "["+data[:-1]+"]"
            data = json.loads(data)
            for item in data:
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
                data = json.dumps(data)
                data = data+","
                data = data.encode("utf-8")
                self.socket.send(data)