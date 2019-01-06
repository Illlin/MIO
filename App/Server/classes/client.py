# Class that will handle the users of the game as an object.

import classes.queue
from threading import Thread    
import json        

class Client:
    # Initialise all the variable for class
    def __init__(self, socket, address, functions):
        Thread.__init__(self)
        self.log = functions["log"]

        self.socket = socket
        self.address = address

        self.alive = True
        self.recv_que = classes.queue.Queue()
        self.send_que = classes.queue.Queue()

        self.valid = False
        self.user_id = None

        self.log("Client_info","Client object started")

    # Spawn threads for the loops so they are none blocking
    def start_loops(self):
        self.log("Client_info","Starting loop")
        self.recv_loop = Recv_loop(self.socket, self.recv_que, self, self.log)
        self.send_loop = Send_loop(self.socket, self.send_que)
        
    def kill(self):
        self.log("Client_info","Client Disconnected")
        self.recv_loop.alive = False
        self.send_loop.alive = False
        self.socket.shutdown(2) # socket.SHUT_RDWR (Evaluated to save an import)


# Thread code to handle loop recv
class Recv_loop(Thread):
    def __init__(self, socket, queue, parent, log, buffer_size=4096):
        Thread.__init__(self)
        self.deamon=True
        self.log = log
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
            try:
                data = json.loads(data)
                for item in data:
                    self.queue.enqueue(item)
            except json.decoder.JSONDecodeError:
                self.log("packet_error", "JSON ERROR!: "+str(data))

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
