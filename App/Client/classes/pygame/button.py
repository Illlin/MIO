# This will be the class type of a button.
import pygame

class Button:
    # Initilisation
    def __init__(self,origin, width, height, text, font, box_colour,text_colour,function, dark = 0.5):
        self.origin = origin
        self.width  = width
        self.height = height
        self.text   = text
        self.font   = font
        self.box_colour = box_colour
        self.hover_colour = (int(box_colour[0]*dark),int(box_colour[0]*dark),int(box_colour[0]*dark))
        self.text_colour = text_colour
        self.function = function
        self.hover=False

    # Move button if needed
    def setPosition(self, origin, width, height):
        self.width  = width
        self.origin = origin
        self.height = height

    # Check if point is a collision
    def pressed(self,mouse):
        if (
            # Check X
            (mouse[0] >= self.origin[0]) and 
            (mouse[0] <= (self.origin[0] + self.width)) and
            # Check Y
            (mouse[1] >= self.origin[1]) and
            (mouse[1]) <= (self.origin[1] + self.height)
            ):
            return True
        else:
            return False

    # Runs the saved function with gui context
    def run_function(self, gui):
        return self.function(gui)

    # Draw the button
    def draw(self, surface, antialias = True):
        # Add button shape
        if not self.hover:
            colour = self.box_colour
        else:
            colour = self.hover_colour
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
