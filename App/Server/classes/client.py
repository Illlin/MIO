# Class that will handle the users of the game as an object.

import classes.queue
import asyncio

class Client:
    # Initialise all the variable for class
    def __init__(self, socket, functions,sleeptime=0.01):
        self.log = functions["log"]
        self.log("Client_info","Client object started")
        self.alive = True
        self.socket = socket
        self.recv_que = classes.queue.Queue()
        self.send_que = classes.queue.Queue()
        self.sleeptime = 0.01

    # Receive data in to the receive queue
    async def recv(self):
        data = await self.socket.recv()
        self.recv_que.enqueue(data)
        self.log("packet_in", "Got  data: " + str(data))

    # Send data from the send queue
    async def send(self):
        if self.send_que.isdata():
            data = self.send_que.dequeue()
            self.log("packet_out", "Send data: " + str(data))
            await self.socket.send(data)

    # These functions loop over the send and recv functions
    async def send_loop(self):
        self.log("Client_info","Send Loop init")
        while self.alive:
            await self.send()
            await asyncio.sleep(self.sleeptime)

    
    async def recv_loop(self):
        self.log("Client_info","Recv Loop init")
        while self.alive:
            await self.recv()
            await asyncio.sleep(self.sleeptime)

    async def run_coroutine(self,coro):
        loop = asyncio.get_event_loop()
        asyncio.run_coroutine_threadsafe(await coro(), loop)

    # Spawn threads for the loops so they are none blocking
    async def start_loops(self):
        self.log("Client_info","Loop point 1")
        await asyncio.gather(
            self.recv_loop(),
            self.send_loop()
        )
