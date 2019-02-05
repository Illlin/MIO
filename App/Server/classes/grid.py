import perlin
import time
import random
import ansi
x = int(268/2)
y = 1000

bg = "green"

recources = {
    "iron":     {"weight":0.15,"char":"  ","colour":"white"},
    "copper":   {"weight":0.20,"char":"  ","colour":"yellow"},
    "silicone": {"weight":0.30,"char":"  ","colour":"magenta"},
    "water":    {"weight":0.60,"char":"  ","colour":"blue"},
    "oil":      {"weight":0.08,"char":"  ","colour":"black"}
}

rec_list = [recources["water"],recources["silicone"],recources["copper"],recources["iron"],recources["oil"]]

x_off = 1000000
y_off = 1000000

hoff = 10900000

zoom = 40
weight = ["  ","░░","▒▒","▓▓","▉▉"]

a = perlin.SimplexNoise()
ansi.set_text("white")
for i in range(y):
    i += hoff
    for j in range(x):
        j += hoff
        flag = False
        for c, r in enumerate(rec_list):
            if not flag:
                point = a.noise2((j+x_off*c)/zoom, (i+y_off*c)/zoom)
                if point > 1-r["weight"]:
                    ansi.set_background(r["colour"])
                    print(r["char"],end="")
                    flag = True
                    ansi.set_background("black")
        if not flag:
            ansi.set_background(bg)
            print("  ",end="")
            ansi.set_background("black")
        
    print("")
    #time.sleep(0.05)

#░ ▒ ▓ ▉
