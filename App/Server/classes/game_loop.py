# Main Game Loop of the game
from threading import Thread

class Game_loop(Thread):
    def __init__(self,users,log,settings):
        Thread.__init__(self)
        self.deamon=True
        self.users = users
        self.log = log
        self.settings = settings
        self.start()
    
    def run(self):
        self.log("Control", "Entering Client Loop")
        while True:
            for client in self.users:
                if client.recv_que.isdata():
                    name = client.recv_que.dequeue()
                    message = "Hello " + name
                    self.log("Control","GOT DATA!")
                    client.send_que.enqueue(message)