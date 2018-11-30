# This will be split up into 2 threads. One that will call user packets into a queue
# and one workers that will spawn off of the queue and handle the packets from the queue.
import classes.queue
import json
from threading import Thread

class Packet_queuer(Thread):
    def __init__(self,users,log,settings):
        Thread.__init__(self)
        self.deamon=True
        self.users = users
        self.log = log
        self.settings = settings
        self.start()
        self.packet_que = classes.queue.Queue()
    
    def run(self):
        self.log("Control", "Packet looper")
        while True:
            # For each connected user
            for user in self.users:
                # In inbound data
                if user.recv_que.isdata():
                    # multiple packets can be lumped in 1 recv item
                    packet_lump = user.recv_que.dequeue()

                    # Packet is JSON object
                    try:
                        packet_lump = json.loads(packet_lump)
                        for i in range(len(packet_lump)):
                            self.packet_que.enqueue({"user":user, "packet":packet_lump[i]})

                    # Invalid Json used to send packet
                    except json.decoder.JSONDecodeError:
                        self.log("packet_error", "JSONDecodeError")
                        user.send_que.enqueue(self.settings.get_data("packet_error_responce"))
                    # Invalid packet IDs
                    except KeyError:
                        self.log("packet_error", "Invalid Packet Key")
                        user.send_que.enqueue(self.settings.get_data("packet_error_responce"))

"""
-----------------------------------------------------------------
|Packet ID   | Description                          | Direction |
-----------------------------------------------------------------
|00          | Network connection and handshake     | Send/Recv |
|01          | Profile management                   | Send/Recv |
|02          | Loggin in                            | Send/Recv |
|03          | Account Setup                        | Send/Recv |
|xx          |                                      |           |
|09          | General Error handeling and reporting| Send/Recv |
|------------|--------------------------------------|-----------|
|10          | World Chunks                         | Send/Recv |
|11          | Code samples                         | Send/Recv |
|12          | Chunk update Send                    | Send/     |
|13          | Chunk Error handeling                | Send/Recv |
|---------------------------------------------------|-----------|
|20          | IDE data settings ect.               | Send/     |
-----------------------------------------------------------------
"""

def none_function():
    pass

# Function peramiter order. (User Class, Packet Data, LoggerFunction, SettingsFunction)
packet_functions = {
     0:none_function,
     1:none_function,
     2:login,
     3:none_function,
     9:none_function,

    10:none_function,
    11:none_function,
    12:none_function,
    13:none_function,

    20:none_function,
}
class Packet_worker(Thread):
    def __init__(self,packet_queue,log,settings):
        Thread.__init__(self)
        self.deamon=True
        self.packet_queue = packet_queue
        self.log = log
        self.settings = settings
        self.start()
        self.packet_que = classes.queue.Queue()
    
    def run(self):
        while self.packet_que.isdata():
            packet = self.packet_que.dequeue()
            user = packet["user"]
            data = packet["packet"]["DATA"]
            id = packet["packet"]["ID"]
            packet_functions[id](user, data, self.log, self.settings)
            

