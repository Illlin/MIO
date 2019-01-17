# This will contain some functions to be used
# by the pygame sections of the code

import pygame

def gui_event_handle(event, gui):
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


def gui_draw(gui):
    for button in gui["buttons"]:
        gui["buttons"][button].draw(gui["screen"])

    for box in gui["boxes"]:
        gui["boxes"][box].draw(gui["screen"])

    for text in gui["texts"]:
        gui["texts"][text].draw(gui["screen"])

def quit_all(gui):
    if gui["connection"] != None:
        gui["connection"].kill()
    quit()