# This will be an object to handle server connection
import classes.socket_handler

class Connection:
    def __init__(self, ip, port):
        self.connected = False
        self.ip = ip
        self.port = port
        self.connection = None

        self.send = None
        self.recv = None
        self.error = ""

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