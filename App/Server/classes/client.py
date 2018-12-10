# Class that will handle the users of the game as an object.

import classes.queue
import asyncio
from threading import Thread            

class Client:
    # Initialise all the variable for class
    def __init__(self, socket, address, functions):
        self.log = functions["log"]

        self.socket = socket
        self.address = address

        self.alive = True
        self.recv_que = classes.queue.Queue()
        self.send_que = classes.queue.Queue()

        self.log("Client_info","Client object started")

    # Spawn threads for the loops so they are none blocking
    async def start_loops(self):
        self.log("Client_info","Starting loop")
        self.recv_loop = Recv_loop(self.socket, self.recv_que)
        self.send_loop = Send_loop(self.socket, self.send_que)
        


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
