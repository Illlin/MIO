# The main menu of the game.

import classes.connection
import pygame
import classes.pygame.button
import classes.pygame.text_line
import classes.pygame.box

def login(gui):
    # Set up connection Class
    connection = classes.connection.Connection(
        gui["settings"].get_data("server_address"),
        gui["settings"].get_data("server_port")
    )
    
    # Try and initiate socket with server
    try:
        connection.connect()
    except Exception as error:
        if error.errno in [111, -2]:
            print("Connection Error")
        else:
            print(error)
        return error.errno

    email    = gui["texts"]["email"].text
    password = gui["texts"]["password"].text

    # Packet for login
    packet = {
        "ID":   2, #LOGIN ID
        "DATA":{
            "email":    email,
            "password": password
        }
    }
    connection.send(packet)

    # Get login packet from server
    responce = connection.wait_recv()
    while responce["ID"] != 2:
        once = connection.wait_recv()

    print(responce)
    


def back(gui):
    gui["exit"] = True


def main(gui_in):

    gui = {
        "buttons":{},
        "texts":{},
        "boxes":{},
        "screen":gui_in["screen"],
        "size":gui_in["size"],
        "settings":gui_in["settings"],
        "menu_font":gui_in["menu_font"],
        "title_font":gui_in["title_font"],
        "exit":False,
        "connection":None
    }
    width, height = gui["size"]
    
    # origin, width, height, text, font, box_colour,text_colour

    start = 0.3

    gui["boxes"]["email"] = classes.pygame.box.Box(
        (int(width*0.1),int(height*start)),
        int(width*0.2),
        int(height*0.1),
        "E-Mail",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
    )

    gui["texts"]["email"] = classes.pygame.text_line.Text_input(
        (int(width*0.35),int(height*start)),
        int(width*0.55),
        int(height*0.1),
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        print
    )

    gui["boxes"]["password"] = classes.pygame.box.Box(
        (int(width*0.1),int(height*(start+0.15))),
        int(width*0.2),
        int(height*0.1),
        "Password",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
    )

    gui["texts"]["password"] = classes.pygame.text_line.Text_input(
        (int(width*0.35),int(height*(start+0.15))),
        int(width*0.55),
        int(height*0.1),
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        print,
        password=True
    )

    gui["buttons"]["login"] = classes.pygame.button.Button(
        (int(width*0.1),int(height*(start+0.3))),
        int(width*0.8),
        int(height*0.1),
        "Sign In",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        login
    )

    gui["buttons"]["back"] = classes.pygame.button.Button(
        (int(width*0.1),int(height*(start+0.45))),
        int(width*0.8),
        int(height*0.1),
        "Back",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        back
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
        gui["screen"].fill((0,0,0))

        # title
        textsurface = gui["title_font"].render("MIO", True, (255,255,255))
        gui["screen"].blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height*0.1 - textsurface.get_height()/2))
        )
        textsurface = gui["menu_font"].render("Sign In", True, (255,255,255))
        gui["screen"].blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height*0.25 - textsurface.get_height()/2))
        )

        for button in gui["buttons"]:
            gui["buttons"][button].draw(gui["screen"])

        for box in gui["boxes"]:
            gui["boxes"][box].draw(gui["screen"])

        for text in gui["texts"]:
            gui["texts"][text].draw(gui["screen"])

        if gui["exit"]:
            return gui


        pygame.display.update()
    