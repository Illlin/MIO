# Sol Steele
# This script Handles settings from an exsternal file

# Imports
import json

# Class
class Settings:
    def __init__(self, location="settings.JSON"):
        self.location = location
        self.load_from_file()

    def load_from_file(self):
        string = ""
        try:
            with open(self.location, "r") as file:
                for line in file:
                    string += line
        except FileNotFoundError:
            pass

        # Attempt to load JSON data from string
        try:
            self.settings = json.loads(string)
        # If fail assume invalid settings
        except json.decoder.JSONDecodeError:
            self.restor_defaults()

    # Write settings to exsternal file
    def write_to_file(self):
        with open(self.location, "w") as file:
            file.write(json.dumps(self.settings))

    # Reset to default configuration
    def restor_defaults(self):
        self.settings = {}

    # Fetch setting data
    def get(self, setting):
        return self.settings[setting]

    # Set setting data
    def set(self, setting, data):
        self.settings[setting] =  data
