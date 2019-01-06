# The game intro screen. Will play before the main menu loads.

import pygame
black = 0,      0,      0
white = 255,    255,    255

def game_intro(screen, size):
    width, height = size
    intro = True
    dejavu = pygame.font.Font("resources/fonts/Dejavu/DejaVuSerif.ttf", 74)

    val = 255
    textsurface = dejavu.render("MIO", True, (val,val,val))

    while intro:
        screen.fill(black)
        screen.blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height/2 - textsurface.get_height()/2))
        )
        val -= 0.1
        textsurface = dejavu.render("MIO", True, (int(val),int(val),int(val)))
        print(int(val))

        pygame.display.update() 
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        if int(val) == 1:
            return