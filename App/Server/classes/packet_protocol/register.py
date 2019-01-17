# File will take a email and password and respond to the packet
import bcrypt
import random
import classes.hash

def gen_code(size=6, char_set="ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"):
    string = ""
    for i in range(size):
        string += random.choice(char_set)
    return string

def main(functions, data):
    data_base = functions["user_db"]

    success = False

    email = data["email"]
    password = data["password"]
    if email == "" or password == "":
        return {"responce":"Email or password field empty.","success":False,"ID":None}

    user_id = data_base.email_id(email)

    # Is email registers yet?
    if user_id == None:
        code = gen_code()
        user_dict = {
            "email":email,
            "password":classes.hash.make_password_hash(password),
            "verify":False,
            "code":code
        }
        data_base.add_user(user_dict)

        # Email the user there code
        functions["email"].send(
            email,
            "MIO E-Mail verification code",
            "Thank you for joining MIO!\nHere is your verification code\n"+code
        )
        return {"responce":"Verification Code Sent","success":True,"ID":user_id}

    else:
        return {"responce":"Email allready in use", "success":False, "ID":None}