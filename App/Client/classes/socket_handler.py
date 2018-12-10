# This will absctract the socket communication to a simple moduel that can be called and used to setup the server
import socket
from threading import Thread
import classes.queue

class Connection(Thread):
    def __init__(self, server_address, server_port):
        Thread.__init__(self)
        self.deamon=True

        self.server_address = server_address
        self.server_port = server_port
        self.recv_que = classes.queue.Queue()
        self.send_que = classes.queue.Queue()

        self.start()

    def run(self):
        self.connected = False
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.server_address, self.server_port))
        Recv_loop(self.socket, self.recv_que)
        Send_loop(self.socket, self.send_que)


# Thread code to handle loop recv
class Recv_loop(Thread):
    def __init__(self, socket, queue, buffer_size=4096):
        Thread.__init__(self)
        self.deamon=True

        self.alive = True
        self.socket = socket
        self.queue = queue
        self.buffer_size=buffer_size

        self.start()
    
    def run(self):
        while self.alive:
            data = self.socket.recv(self.buffer_size).decode("utf-8")
            self.queue.enqueue(data)

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
                data = data.encode("utf-8")
                self.socket.send(data)