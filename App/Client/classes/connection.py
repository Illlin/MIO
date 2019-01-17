# This will be an object to handle server connection
import classes.socket_handler

class Connection:
    def __init__(self, ip, port):
        self.alive = True
        self.connected = False
        self.ip = ip
        self.port = port
        self.connection = None

        self.send = None
        self.recv = None
        self.error = ""

        self.user_id = None

    def connect(self):
        self.connection = classes.socket_handler.Connection(self.ip, self.port)
        # Wait for start section
        while not self.connection.started:
            pass
        # Check for errors
        if self.connection.halt:
            self.error = self.connection.error
            raise self.error
        else:    
            self.connected = True
            self.send = self.connection.send
            self.recv = self.connection.recv    

    def wait_recv(self):
        get = None
        while get == None:
            get = self.recv()
        return get

    def kill(self):
        self.alive = False
        self.connection.send_loop.alive = False
        self.connection.recv_loop.alive = False
        self.connection.socket.shutdown(2) # socket.SHUT_RDWR (Evaluated to save an import)
