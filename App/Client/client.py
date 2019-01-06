#!/usr/bin/python3.7

# Sol Steele 2018

# This is the game client that will run the app
#import pygame 
import sys
import classes.socket_handler
import pygame
import classes.json_file

import screens.intro
import screens.main_menu

# Set up constants for use
size = width, height = 640, 480
black = 0,      0,      0
white = 255,    255,    255

settings = classes.json_file.Json_file("resources/settings.JSON")

# Set up PyGame Screen
def main():
    # Initilise pygame objects
    pygame.init()
    pygame.font.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('MIO')
    #screens.intro.game_intro(screen, size)
    screens.main_menu.main(screen, size, settings)

def start_connection(address, port):
    connection = classes.socket_handler.Connection(address, port)
    return connection

if __name__ == "__main__":
    main()

