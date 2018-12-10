# Sol Steele 2018

# This is the game client that will run the app
#import pygame 
import sys
import classes.socket_handler

# Set up constants for use
size = width, height = 640, 480
black = 0,      0,      0
white = 255,    255,    255

# Set up PyGame Screen
def main():
    pygame.init()

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('MIO')
    clock = pygame.time.Clock()
    
    game_intro(screen)

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    



def start_connection(address, port):
    connection = classes.socket_handler.Connection(address, port)
    return connection

if __name__ == "__main__":
    connection = start_connection("127.0.0.1",5678)
    print("Connected!")


