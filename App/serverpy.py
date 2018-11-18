# Sol Steele
# Initial server test

import asyncio  # Handles asyncrodous input output
import websockets  # Handles webosocket connectiuons
import threading

class client:
    def __init__(self, socket, deamon=False):
        self.socket = socket
        self.que = queue()
        self.deamon = deamon
        if self.deamon:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.recv_to_queue())
            print("Setup wait")
    
    # Return queued messages
    def recv(self):
        if self.que.isdata:
            return self.que.dequeue()
        else:
            return None

    # Send data
    async def send(self,data):
        await self.socket.send(data)

    # Get message and add to queue
    async def recv_to_queue(self):
        #data = await self.socket.recv()
        data = self.socket.recv()
        self.que.enqueue(data)

    # Blocking function to be called from thread to add messages to the queue
    async def connection_daemon(self):
        pass

# Implementation of a queue
class queue:
    def __init__(self):
        self.queue = []

    # Dequeue from list, return None if no data
    def dequeue(self):
        if len(self.queue) > 0:
            data = self.queue[0]
            del self.queue[0]
            return data
        else:
            return None
    
    # Add data to the que
    def enqueue(self,data):
        self.queue.append(data)

    # Return length of queue
    def len(self):
        return len(self.queue)

    # Return true if queue has data
    def isdata(self):
        return self.len() != 0

async def run_socket(ws, path):
    # define message que
    """
    user = client(ws,deamon=False)
    #start listening for next message with out blocking code
    print("Connection")
    # wait till message has arrived
    await user.recv_to_queue()
    data = user.recv()
    """
    user = client(ws)
    print("Connection")
    while True:
        print(dir(user.recv_to_queue()))
    data = user.recv()
    while data == None:
        data = user.recv()
    name = data
    print(name)

    # respond with greeting
    await user.send("Hello " + name)
    print("Connection Closed")

# Name function to start server
start_server = websockets.serve(run_socket, 'localhost', 5678)

print("Start")
# Define main loop
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
print("Enter Loop")
asyncio.get_event_loop().run_forever()
