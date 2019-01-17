# Main Game Loop of the game


from threading import Thread
import classes.queue
import classes.packet_protocol.login
import classes.packet_protocol.register
import classes.packet_protocol.verify

# Main game loop
def main_loop(users,log,settings, functions):

    # Read packets into queue for handeling
    validate_queue = classes.queue.Queue()
    work_queue = classes.queue.Queue()
    for client in users:
        while client.recv_que.isdata():
            # They are a verified User
            packet = (client,client.recv_que.dequeue())
            if client.valid:
                work_queue.enqueue(packet)

            # Packet Queue for non logged in users.
            else:
                validate_queue.enqueue(packet)

    # Go through validate queue and log in users.
    while validate_queue.isdata():
        client, packet = validate_queue.dequeue()
        try:
            if packet["ID"] == 2:    # Log In, Only packet to respond to with un-authorised users
                success = classes.packet_protocol.login.main(functions, packet["DATA"])
                responce = {"ID":2,"DATA":success}
                if success["success"] == True:
                    client.valid = True
                    client.user_id = success["ID"]
                    log("Client_Connect",str(client.user_id) + " Connected.")
                if success["success"] == "verify":
                    responce = {"ID":2,"DATA":success}
                    log("Client_Connect",str(client.user_id) + " Connected. Need Verification")


            elif packet["ID"] == 3:   # Set up account
                success = classes.packet_protocol.register.main(functions, packet["DATA"])
                log("Client_Connect","Account register " + str(success["ID"]))
                responce = {"ID":3,"DATA":success}

            elif packet["ID"] == 4:   # Check verification code
                success = classes.packet_protocol.verify.main(functions, packet["DATA"])
                log("Client_Connect","Account code verification")
                responce = {"ID":4, "DATA":success}



            
            else:
                responce = {"ID":9,"DATA":"INVALID PACKET, CLIENT NOT VERIFIED"}

            client.send_que.enqueue(responce)
        except ReferenceError as e:
            log("Server_Error","Error in Validate queue: " + str(e))
            
            


class Game_loop(Thread):
    def __init__(self,functions):
        Thread.__init__(self)
        self.deamon=True

        self.functions = functions
        self.users = functions["users"]
        self.log = functions["log"]
        self.settings = functions["settings"]
        self.alive = True

        self.start()
    
    def run(self):
        self.log("Control", "Entering Client Loop")
        while self.alive:
            main_loop(self.users,self.log,self.settings,self.functions)