# This will be the class type of a button.
import pygame

class Box:
    # Initilisation
    def __init__(self,origin, width, height, text, font, box_colour,text_colour):
        self.origin = origin
        self.width  = width
        self.height = height
        self.text   = text
        self.font   = font
        self.box_colour = box_colour
        self.text_colour = text_colour

    # Move button if needed
    def setPosition(self, origin, width, height):
        self.width  = width
        self.origin = origin
        self.height = height


    # Draw the button
    def draw(self, surface, antialias = True):
        # Add button shape
        colour = self.box_colour

        pygame.draw.rect(
            surface,
            colour,
            (self.origin[0], self.origin[1], self.width, self.height)
            )
        
        # Make text object
        textsurface = self.font.render(self.text, antialias, self.text_colour)

        # Draw text over button (Don't check if it will fit, just assume)
        surface.blit(
            textsurface,
            (
                int((self.width/2 + self.origin[0]) - textsurface.get_width()/2),
                int((self.height/2 + self.origin[1]) - textsurface.get_height()/2)
            )
        )
