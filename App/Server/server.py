#!/usr/bin/python3.7
# Sol Steele
# Python Server

# Import custom classes
import classes.json_file
import classes.logger
import classes.client
import classes.game_loop
import classes.user_dbms
import classes.email

# Import libereys for threading and websockets

import threading
import socket


users = []
alive = True

# load settings
settings = classes.json_file.Json_file("settings.JSON")

# Load user database
data_base = classes.user_dbms.UserDB(settings.get_data("file_location"))

# Setup loggger
logger = classes.logger.Log(settings.get_data("log_file"))
log = logger.log

# Will be used to pass classes to sub-processes by reference
functions = {
    "log":log,
    "settings":settings,
    "users":users,
    "user_db":data_base
}

# Read user data base to json file object

# Used when a user connects to the server
def setup_user(socket, address):
    # Set up client object
    current_client = classes.client.Client(socket,address,functions)

    # Add user to list of connected users
    users.append(current_client)

    # Start the IO threads for the clients
    current_client.start_loops()


# Running in function so can be called by external file if needed.
def main():
    # Set Up Email client
    log("Control", "Starting Email Session")
    functions["email"] = classes.email.Email(settings)


    log("Control", "Starting User Thread")

    # Start Game loop thread
    classes.game_loop.Game_loop(functions)

    log("Control", "Start Server Thread")

    # Start server object
    
    log("Control", "Server Starting")
    # Setup the server thread
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Allow port re-use
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind socket
    server_socket.bind((
        settings.get_data("server_address"),
        settings.get_data("server_port")
    ))

    server_socket.listen(5)
    while alive:
        # Accept connection
        client_socket, client_address = server_socket.accept()
        log("Connection", "Connection from " + str(client_address))

        # Set up the user and spawn connection threads
        setup_user(client_socket, client_address)


main()