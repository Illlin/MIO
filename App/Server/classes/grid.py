import perlin
import time
import random
import ansi
x = 268
y = 1000

bg = "green"

recourses = {
    "iron":     {"weight":0.15,"zoom":40,"char":" ","colour":"white"},
    "copper":   {"weight":0.20,"zoom":40,"char":" ","colour":"yellow"},
    "silicone": {"weight":0.10,"zoom":20,"char":" ","colour":"magenta"},
    "water":    {"weight":0.40,"zoom":80,"char":" ","colour":"blue"},
    "oil":      {"weight":0.08,"zoom":40,"char":" ","colour":"black"}
}

rec_list = [recourses["water"],recourses["silicone"],recourses["copper"],recourses["iron"],recourses["oil"]]

x_off = 1000000
y_off = 1000000

hoff = 0

zoom = 40
weight = ["  ","░░","▒▒","▓▓","▉"]

a = perlin.SimplexNoise()
ansi.set_text("white")
for i in range(y):
    i += hoff
    for j in range(x):
        j += hoff
        flag = False
        for c, r in enumerate(rec_list):
            if not flag:
                point = a.noise2((j*0.5+x_off*c)/r["zoom"], (i+y_off*c)/r["zoom"])
                if point > 1-r["weight"]:
                    ansi.set_background(r["colour"])
                    print(r["char"],end="")
                    flag = True
                    ansi.set_background("black")
        if not flag:
            ansi.set_background(bg)
            print(" ",end="")
            ansi.set_background("black")
        
    print("")
    #time.sleep(0.05)

#░ ▒ ▓ ▉
