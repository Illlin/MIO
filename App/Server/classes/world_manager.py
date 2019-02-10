# This will hold the objects responsble for the world

# ---- imports ----
import os
import classes.perlin


def make_chunk(chunk_y,chunk_x,settings):
    chunk_size = settings.get_data("chunk_size") 
    offset = settings.get_data("offset")
    #Load recourses weights and values
    recourses = settings.get_data("recourses")
    # Turn in to iterable list
    rec_list = []
    for i in settings.get_data("rec_list_order"):
        rec_list.append(recourses[i])

    a = classes.perlin.SimplexNoise()
    chunk = []
    for i in range(chunk_size):
        chunk.append([" "]*chunk_size)

    for x in range(chunk_size):
        rel_x = x+chunk_size*chunk_x

        for y in range(chunk_size):
            rel_y = y+chunk_size*chunk_y
            active_tile = False
            for index, rec in enumerate(rec_list):
                if not active_tile:
                    point = a.noise2(
                        (rel_x+offset*index)/rec["zoom"],
                        (rel_y+offset*index)/rec["zoom"],)
                        
                        #(x+offset*index)/rec["zoom"],
                        #(y+offset*index)/rec["zoom"])
                
                    if point > 1-rec["weight"]:
                        chunk[x][y] = rec["char"]
        print(x)
    return chunk


    

    


def load_chunk(x,y,settings):
    name = "storage/world/"+str(x)+"x"+str(y)
    if os.path.isdir(name):
        pass
    else:
        os.mkdir(name)
        chunk = make_chunk(x,y, settings)
        with open(name+"/chunk.dat","w") as file:
            for row in chunk:
                for char in row:
                    file.write(char)
                file.write("\n")