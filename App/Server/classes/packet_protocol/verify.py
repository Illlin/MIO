import bcrypt

def main(functions, data):
    data_base = functions["user_db"]

    success = False

    email = data["email"]
    password = data["password"]
    code = data["code"]

    user_id = data_base.email_id(email)

    # User exists, check password
    if user_id != None:
        user_info = data_base.get_info(user_id)
        user_hash = user_info["password"]    
        success = bcrypt.checkpw(password.encode("utf-8"),user_hash.encode("utf-8"))
        
        # They don't have corret password
        if not success:
            return {"responce":"Email or password are invalid","success":False,"ID":None}    

        if user_info["code"] == code:
            data_base.remove_field(user_id, "code")
            data_base.change_info(user_id, {"verify":True})
            return {"responce":"User account verified", "success":True,"ID":user_id}
            functions["email"].send(
                email,
                "Thank you for joining MIO",
                "Your MIO account has be verified."
            )

        else:
            return {"responce":"Invalid Code","success":False,"ID":user_id}
        

    else:
        return {"responce":"Email or password are invalid","success":False,"ID":None}