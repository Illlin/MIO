# Main Game Loop of the game
# TODO Rewrite LOOP

from threading import Thread

# Main game loop
def main_loop(users,log,settings):
    for client in users:
        if client.recv_que.isdata():
            name = client.recv_que.dequeue()
            message = "Hello " + name
            log("Game_info","Got data")
            client.send_que.enqueue(message)
            client.send_que.enqueue("So, This is message 2")
            
            while not client.recv_que.isdata():
                pass
            m1 = client.recv_que.dequeue()
            while not client.recv_que.isdata():
                pass
            m2 = client.recv_que.dequeue()
            log("Game_info", "Got: " + m1 + m2)

class Game_loop(Thread):
    def __init__(self,functions):
        Thread.__init__(self)
        self.deamon=True

        self.functions = functions
        self.users = functions["users"]
        self.log = functions["log"]
        self.settings = functions["settings"]

        self.start()
    
    def run(self):
        self.log("Control", "Entering Client Loop")
        while True:
            main_loop(self.users,self.log,self.settings)