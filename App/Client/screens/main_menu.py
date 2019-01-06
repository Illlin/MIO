# The main menu of the game.

import classes.connection
import pygame
import classes.pygame.button
import classes.pygame.text_line

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
        pygame.quit
    )


    while True:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in gui["buttons"]:
                    if gui["buttons"][button].pressed(event.pos):
                        gui["buttons"][button].run_function(gui)
                for text in gui["texts"]:
                    if gui["texts"][text].pressed(event.pos):
                        gui["texts"][text].click(event.pos)
                    else:
                        gui["texts"][text].focus = False

            if event.type == pygame.MOUSEMOTION:
                for button in gui["buttons"]:
                    if gui["buttons"][button].pressed(event.pos):
                        gui["buttons"][button].hover = True
                    else:
                        gui["buttons"][button].hover = False

            if event.type == pygame.KEYDOWN:
                for text in gui["texts"]:
                    if gui["texts"][text].focus:
                        gui["texts"][text].add_char(event.unicode, event.key, event.mod)

        # Begin screen draw function
        screen.fill((0,0,0))

        # title
        textsurface = gui["title_font"].render("MIO", True, (255,255,255))
        screen.blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height*0.1 - textsurface.get_height()/2))
        )

        for button in gui["buttons"]:
            gui["buttons"][button].draw(screen)

        for text in gui["texts"]:
            gui["texts"][text].draw(screen)


        pygame.display.update()
    
    
