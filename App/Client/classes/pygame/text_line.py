import pygame

class Text_input:
    #Initilisation
    def __init__(self, origin, width, height, font, box_colour, text_colour, function, border = 0.05, password = False):
                       
        # Copy Args to name space
        self.font           = font
        self.origin         = origin
        self.width          = width
        self.height         = height
        self.box_colour     = box_colour
        self.text_colour    = text_colour
        self.border         = border
        self.password       = password
        self.function       = function

        self.focus          = False
        self.position_ln    = 0
        self.position_px    = 0
        self.text           = ""

    # Used for reading single bits from a number, used in keyboard mods
    def get_bit(self,byteval,idx):
        return ((byteval&(1<<idx))!=0)

    def rendered_text(self):
        if self.password:
            return len(self.text)*"*"
        else:
            return self.text

    def run_function(self):
        self.function(self.text)

    def add_char(self, char, key, mod):
        text_before = self.font.render(self.rendered_text(), False, self.text_colour).get_width()
        text_before_pos = self.font.render(self.rendered_text()[:self.position_ln], False, self.text_colour).get_width()
        text_box_width = int(self.width - self.width*(self.border*2))

        #BackSpace
        if char == "\x08":
            # Remove character before line position
            if self.position_ln > 0:
                self.text = self.text[:self.position_ln-1]+ self.text[self.position_ln:]
                self.position_ln -= 1
                text_after = self.font.render(self.rendered_text(), False, self.text_colour).get_width()

                self.position_px += text_after-text_before

                if self.position_px < 0:
                    self.position_px = 0

        #enter/return:
        elif char == "\r":
            #Run linked function
            self.run_function()

        #LEFT
        elif key == pygame.K_LEFT:
            self.position_ln -= 1
            if self.position_ln < 0:
                self.position_ln = 0
            text_after_pos = self.font.render(self.rendered_text()[:self.position_ln], False, self.text_colour).get_width()
            self.position_px += text_after_pos-text_before_pos
            if self.position_px < 0:
                self.position_px = 0

        #RIGHT
        elif key == pygame.K_RIGHT:
            self.position_ln += 1
            if self.position_ln > len(self.text):
                self.position_ln = len(self.text)
            text_after_pos = self.font.render(self.rendered_text()[:self.position_ln], False, self.text_colour).get_width()
            self.position_px += text_after_pos-text_before_pos
            if self.position_px > text_box_width:
                self.position_px = text_box_width
        
        #Home
        elif key == pygame.K_HOME:
            self.position_ln = 0
            self.position_px = 0
        
        #END
        elif key == pygame.K_END:
            self.position_ln = len(self.text)
            if text_before >= text_box_width:
                self.position_px = text_box_width
            else:
                self.position_px = text_before

        #CTRL+U (Clear input)
        elif key == pygame.K_u and (self.get_bit(mod,6) or self.get_bit(mod,7)):
            self.position_ln    = 0
            self.position_px    = 0
            self.text           = ""

        elif char != "":

            self.text = self.text[:self.position_ln] + char + self.text[self.position_ln:]
            self.position_ln += 1
            text_after = self.font.render(self.rendered_text(), False, self.text_colour).get_width()
            self.position_px += text_after-text_before

            # Check if over box position
            if self.position_px > text_box_width:
                self.position_px = text_box_width

        print(self.text)
        print(len(self.text))


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

    # When item is clicked
    def click(self, pos):
        self.focus = True

        # Text area
        current_width = self.font.render(self.rendered_text()[:self.position_ln], False, (0,0,0)).get_width()

        # Goal position across screen.
        mouse_x =  current_width - self.position_px - self.width*self.border - self.origin[0] + pos[0]

        # Find closes position to where was clicked
        short = [0,float("inf")] # index, distance
        for i in range(len(self.text)+1):
            distance = abs(mouse_x - self.font.render(self.rendered_text()[:i], False, (0,0,0)).get_width())
            if distance < short[1]:
                short[1] = distance
                short[0] = i

        # Short now contains the closest point to where was clicked
        width = self.font.render(self.rendered_text()[:short[0]], False, (0,0,0)).get_width()
        anchor = current_width - self.position_px

        # Within allready existing box create new cursor position.
        self.position_ln = short[0]
        self.position_px = width - anchor
        

    def draw(self, surface, antialias = True):
        # Add button shape
        pygame.draw.rect(
            surface,
            self.box_colour,
            (self.origin[0], self.origin[1], self.width, self.height)
        )
        
        # Make text object
        textsurface = self.font.render(self.rendered_text(), antialias, self.text_colour)
        text_before = self.font.render(self.rendered_text()[:self.position_ln], False, self.text_colour)

        # Check if text will fit.
        # |border TEXT border|
        # Border provides padding so text does not clash with box

        text_box_width = int(self.width - self.width*(self.border*2))

        # Text box fits
        if textsurface.get_width() <= text_box_width:
            surface.blit(
                textsurface,
                (
                    int(self.origin[0] + self.width*self.border),   #X
                    int(self.origin[1] + self.height*self.border)   #Y
                )
            )
                
        # Text does not fit and needs scrolling
        else:
            left_side = text_before.get_width() - self.position_px
            right_side = textsurface.get_width() - left_side - text_box_width

            # Blit cropped text section to screen
            surface.blit(
                textsurface,
                (
                    int(self.origin[0] + self.width*self.border),   #X
                    int(self.origin[1] + self.height*self.border)   #Y
                ),
                (
                    left_side, 0,                                   # X,Y
                    text_box_width, textsurface.get_height(),       # W,H
                )
            )

        
        # Draw cursor
        if self.focus:
            x = int(self.origin[0] + self.width*self.border + self.position_px)
            y = int(self.origin[1] + self.height*(self.border))
            pygame.draw.rect(
                    surface,
                    self.text_colour,
                    (
                        x,
                        y,
                        2,
                        self.height*(1-self.border))
                )
            
            

