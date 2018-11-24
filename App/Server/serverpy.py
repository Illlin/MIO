#!/usr/bin/python3
# Sol Steele
# Initial server test

import asyncio  # Handles asyncrodous input output
import websockets  # Handles webosocket connectiuons
import threading
from classes.queue import Queue

class client:
    def __init__(self, socket):
        self.socket = socket
        self.que = Queue()

    
    # Return queued messages
    def recv(self):
        if self.que.isdata():
            return self.que.dequeue()
        else:
            return None


    # Send data
    async def send(self,data):
        await self.socket.send(data)


    # Get message and add to queue
    async def recv_to_queue(self):
        data = await self.socket.recv()
        self.que.enqueue(data)


    async def summon_deamon(self):
        self.deamon_task = asyncio.create_task(
                self.deamon_loop()
            )
        return self.deamon_task


    async def deamon_loop(self):
        print("DEAMON UP")
        while True:
            await self.recv_to_queue()
            print("DEAMON TEST")


async def socket_code(user):
    print("Connection")
    name = user.recv()
    while name == None:
        name = user.recv()
    print(name)

    # respond with greeting
    await user.send("Hello " + name)
    print("Connection Closed")

async def run_socket(ws, path):
    user = client(ws)
    loop.run_in_executor(user.summon_deamon())
    asyncio.run(socket_code(user))

# Name function to start server
start_server = websockets.serve(run_socket, 'localhost', 5678)

print("Start")
# Define main loop
loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
print("Enter Loop")
asyncio.get_event_loop().run_forever()
