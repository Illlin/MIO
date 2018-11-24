# This code will be responsible for provieing loggin information and file logging for debug.
import classes.json_file
import classes.ansi
import datetime

class Log:
    def __init__(self,log_file,settings_file="logging.JSON"):
        self.settings = classes.json_file.Json_file(settings_file)
        self.log_file = log_file

    # Get the current time of the system.
    def get_time(self):
        return str(datetime.datetime.now())


    # Write line to text file
    def log_to_file(self, text):
        with open(self.log_file, "a") as file:
            file.write(text)

    # print and write to file:
    def log(self, log_type, text):
        # Get time of logging event
        time = self.get_time()
        type_setting = self.settings.get_data(log_type)

        # Form that the log will be printed in
        form = "<<" + time + ">> " + log_type + ": " + text + "\n"

        # Print text according to settings
        if type_setting["display"]:
            classes.ansi.colour_print(form, tx=type_setting["colour"],end="")
        # Write it to the log file.
        self.log_to_file(form)

    # Remove log file.
    def purge_log(self):
        with open(self.log_file,"w") as file:
            file.write("Log Purged - " + self.get_time())
        
