#!/usr/bin/python3.7
# Sol Steele
# Python Server

# Import custom classes
import classes.json_file
import classes.logger
import classes.client
import classes.game_loop

# Import libereys for threading and 
import asyncio
import threading
import websockets

users = []

# load settings
settings = classes.json_file.Json_file("settings.JSON")

# Setup loggger
logger = classes.logger.Log(settings.get_data("log_file"))
log = logger.log

functions = {
    "log":log,
    "settings":settings,
    "users":users
}

async def setup_user(socket, path):
    log("Client", "Client Connected")
    current_client = classes.client.Client(socket,functions)
    users.append(current_client)
    log("Client", "Client Entering Loop")
    await current_client.start_loops()

# Running in function so can be called by external file if needed.
def main():
    log("Control", "Starting User Thread")
    # Start Game loop thread
    classes.game_loop.Game_loop(functions)

    log("Control", "Start Server Thread")
    # Pass event loop to Server for it to run.
    loop = asyncio.get_event_loop()
    
    log("Control", "Server Starting")
    # Setup the server async coroutine
    start_server = websockets.serve(
        setup_user, # Bound function
        settings.get_data("server_address"), 
        settings.get_data("server_port"),
    )    

    log("Control", "Socket Object Started")
    loop.run_until_complete(start_server)
    log("Control", "Enterting Server Loop")
    asyncio.get_event_loop().run_forever()


main()