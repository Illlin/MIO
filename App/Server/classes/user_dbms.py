# Function to mange the user database
#
#   USERID{
#       "email":"abc@123.com"
#       "password":b'$2b$12$/rGkFBOVAOhnDj5NhXKB3.aF8LNUwwqpN3zFCRAIoiXQ2rSm1uzOS'
#   }
#
#

import random
import classes.json_file

class UserDB:
    def __init__(self,location):
        location = location+"users/user_login.JSON"
        self.db = classes.json_file.Json_file(location)
        self.char_set = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-="

    #Get ID from email
    def email_id(self, email):
        for user in self.db.json:
            if self.db.json[user]["email"] == email:
                return user
        return None

    # Get info of a user from there ID
    def get_info(self,user_id):
        return self.db.get_data(user_id)

    # Update user info and write to file
    def change_info(self,user_id,update_dict):
        for field in update_dict:
            self.db.json[user_id][field] = update_dict[field]
        self.db.write_to_file()

    def gen_id(self,size=32):
        success = False
        while not success:
            # Make UUID
            uuid = ""
            for i in range(size):
                uuid += random.choice(self.char_set)

            # Check not in use
            if uuid not in self.db.json:
                success = True

        return uuid
        

    def add_user(self,info_dict):
        self.db.set_data(self.gen_id(),info_dict)
        self.db.write_to_file()

    def remove_field(self,user_id,field):
        del self.db.json[user_id][field]
