# The main menu of the game.

import classes.connection
import pygame
import classes.pygame.button
import classes.pygame.text_line
import classes.pygame.functions
import screens.login


def draw_center(text, screen, font, size):
    width, height = size
    textsurface = font.render(text, True, (255,255,255))
    screen.blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height/2 - textsurface.get_height()/2))
        )

def main(screen, size, settings):
    width, height = size

    screen.fill((0,0,0))
    dejavu = pygame.font.Font("resources/fonts/Dejavu/DejaVuSans.ttf", 20)
    dejavu_70 = pygame.font.Font("resources/fonts/Dejavu/DejaVuSerif.ttf", 70)
    pygame.display.update()
    
    gui = {
        "buttons":{},
        "texts":{},
        "boxes":{},
        "screen":screen,
        "size":size,
        "settings":settings,
        "menu_font":dejavu,
        "title_font":dejavu_70,
        "connection":None
    }

    gui["texts"]["test"] = classes.pygame.text_line.Text_input(
        (int(width*0.1),int(height*0.65)),
        int(width*0.8),
        int(height*0.1),
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        print
    )

    gui["buttons"]["Sign In"] = classes.pygame.button.Button(
        (int(width*0.1),int(height*0.2)),
        int(width*0.8),
        int(height*0.1),
        "Sign In",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        screens.login.main
    )
    
    gui["buttons"]["Settings"] = classes.pygame.button.Button(
        (int(width*0.1),int(height*0.35)),
        int(width*0.8),
        int(height*0.1),
        "Settings",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        print
    )
    
    gui["buttons"]["Quit"] = classes.pygame.button.Button(
        (int(width*0.1),int(height*0.50)),
        int(width*0.8),
        int(height*0.1),
        "Quit",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        classes.pygame.functions.quit_all
    )


    while True:
        for event in pygame.event.get():
            classes.pygame.functions.gui_event_handle(event, gui)

        # Begin screen draw function
        screen.fill((0,0,0))

        # title
        textsurface = gui["title_font"].render("MIO", True, (255,255,255))
        screen.blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height*0.1 - textsurface.get_height()/2))
        )

        classes.pygame.functions.gui_draw(gui)


        pygame.display.update()
    
    
