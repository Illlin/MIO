# Sol Steele
# This script Handles settings from an external file

# Imports
import json

# Class
class Json_file:
    def __init__(self, location):
        self.location = location
        self.load_from_file()

    def load_from_file(self):
        string = ""
        try:
            with open(self.location, "r") as file:
                for line in file:
                    string += line
        except FileNotFoundError:
            # If file not found keep string as ""
            pass

        # Attempt to load JSON data from string
        try:
            self.json = json.loads(string)
        # If fail assume invalid json
        except json.decoder.JSONDecodeError:
            self.restor_defaults()

    # Write json to exsternal file
    def write_to_file(self):
        with open(self.location, "w") as file:
            file.write(json.dumps(self.json))

    # Reset to default configuration
    def restor_defaults(self):
        self.json = {}

    # Fetch json data
    def get_data(self, id):
        return self.json[id]

    # Set json data
    def set_data(self, id, data):
        self.json[id] =  data
