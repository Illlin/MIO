import classes.connection
import pygame
import classes.pygame.button
import classes.pygame.text_line
import classes.pygame.box
import classes.pygame.functions
import classes.pygame.popup as popup

def back(gui):
    gui["exit"] = True

def verify(gui):
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
    code     = gui["texts"]["code"].text


    # Packet for login
    packet = {
        "ID":   4, #LOGIN ID
        "DATA":{
            "email":    email,
            "password": password,
            "code":     code
        }
    }
    connection.send(packet)
    responce = connection.wait_recv()
    while responce["ID"] != 4:
        responce = connection.wait_recv()
    popup.popup(responce["DATA"]["responce"])
    if responce["DATA"]["success"] == True:
        back(gui)
    


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
        "connection":None,
        "ext_gui":gui_in
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

    gui["boxes"]["code"] = classes.pygame.box.Box(
        (int(width*0.1),int(height*(start+0.3))),
        int(width*0.2),
        int(height*0.1),
        "Code",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
    )

    gui["texts"]["code"] = classes.pygame.text_line.Text_input(
        (int(width*0.35),int(height*(start+0.3))),
        int(width*0.55),
        int(height*0.1),
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        print
    )

    gui["buttons"]["register"] = classes.pygame.button.Button(
        (int(width*0.1),int(height*(start+0.45))),
        int(width*0.8),
        int(height*0.1),
        "Register",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        verify
    )

    gui["buttons"]["back"] = classes.pygame.button.Button(
        (int(width*0.1),int(height*(start+0.6))),
        int(width*0.8),
        int(height*0.1),
        "Back",
        gui["menu_font"],
        (24,24,24),
        (255,255,255),
        back
    )

    gui["texts"]["email"].text = gui_in["texts"]["email"].text
    gui["texts"]["password"].text = gui_in["texts"]["password"].text


    while True:
        for event in pygame.event.get():
            classes.pygame.functions.gui_event_handle(event, gui)

        # Begin screen draw function
        gui["screen"].fill((0,0,0))

        # title
        textsurface = gui["title_font"].render("MIO", True, (255,255,255))
        gui["screen"].blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height*0.1 - textsurface.get_height()/2))
        )
        textsurface = gui["menu_font"].render("Verify Account", True, (255,255,255))
        gui["screen"].blit(
            textsurface,
            (int(width/2 - textsurface.get_width()/2),int(height*0.25 - textsurface.get_height()/2))
        )

        classes.pygame.functions.gui_draw(gui)

        if gui["exit"]:
            return gui


        pygame.display.update()