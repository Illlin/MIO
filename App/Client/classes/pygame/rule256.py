# Uses the 256Rule set to generate a background


import pygame as pg
import random
import time
import math

pg.init()
size = width, height = 512,512
screen = pg.display.set_mode(size)
pixel_size = 8
width = math.ceil(width/pixel_size)
height = math.ceil(height/pixel_size)

while True:
    rule = ""
    bg = (31,31,31)
    fg = (0,0,0)

    for x in range(0,8):
        rule += str(random.randint(0,1))

    line = []
    nextline = []

    for i in range(0,width):
        line.append(str(random.randint(0,1)))

    '''for i in range(0,400):
        line.append("0")
    line.append("1")
    for i in range(0,399):
        line.append("0")'''

    for y in range(0, height):

        for point in range(0,len(line)):
            pixel = (point*pixel_size, y*pixel_size, pixel_size, pixel_size)
            if line[point] == "1":
                pg.draw.rect(screen, fg, pixel)
            else:
                pg.draw.rect(screen, bg, pixel)
                    
        group = [line[width-1],line[0],line[1]]
        
        if group == ["1","1","1"]:
            nextline.append(rule[0])
        elif group == ["1","1","0"]:
            nextline.append(rule[1])
        elif group == ["1","0","1"]:
            nextline.append(rule[2])
        elif group == ["1","0","0"]:
            nextline.append(rule[3])
        elif group == ["0","1","1"]:
            nextline.append(rule[4])
        elif group == ["0","1","0"]:
            nextline.append(rule[5])
        elif group == ["0","0","1"]:
            nextline.append(rule[6])
        elif group == ["0","0","0"]:
            nextline.append(rule[7])
            
        for index in range(0,width-2):
            group = line[index:index+3]
            if group == ["1","1","1"]:
                nextline.append(rule[0])
            elif group == ["1","1","0"]:
                nextline.append(rule[1])
            elif group == ["1","0","1"]:
                nextline.append(rule[2])
            elif group == ["1","0","0"]:
                nextline.append(rule[3])
            elif group == ["0","1","1"]:
                nextline.append(rule[4])
            elif group == ["0","1","0"]:
                nextline.append(rule[5])
            elif group == ["0","0","1"]:
                nextline.append(rule[6])
            elif group == ["0","0","0"]:
                nextline.append(rule[7])
                
        group = [line[width-2],line[width-1],line[0]]

        if group == ["1","1","1"]:
            nextline.append(rule[0])
        elif group == ["1","1","0"]:
            nextline.append(rule[1])
        elif group == ["1","0","1"]:
            nextline.append(rule[2])
        elif group == ["1","0","0"]:
            nextline.append(rule[3])
        elif group == ["0","1","1"]:
            nextline.append(rule[4])
        elif group == ["0","1","0"]:
            nextline.append(rule[5])
        elif group == ["0","0","1"]:
            nextline.append(rule[6])
        elif group == ["0","0","0"]:
            nextline.append(rule[7])


        line = nextline
        nextline = []

        pg.display.flip()
        time.sleep(0.02)
    time.sleep(2)
