# File will take a email and password and respond to the packet
import bcrypt


def main(functions, data):
    data_base = functions["user_db"]

    success = False

    email = data["email"]
    password = data["password"]

    user_id = data_base.email_id(email)

    # User exists, check password
    if user_id != None:
        user_hash = data_base.get_info(user_id)["password"]  
        success = bcrypt.checkpw(password.encode("utf-8"),user_hash.encode("utf-8"))  

    if success:
        return {"responce":"Log In Successful","success":True,"ID":user_id}
    else:
        return {"responce":"Email or password are invalid","success":False,"ID":None}