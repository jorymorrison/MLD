from pathlib import Path
import json
import glob, os

try:
    file = open ("config.conf", "r")

except IOError as er:
    print("Missing file path:\n" + "config.conf\n")
    try:
        keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
        print(keys)
    except KeyError as er:
        print(
            "Missing environment variables:\nWATSON_USER\nWATSON_PASS\n")
        RunRequest = input ("Please run a set-up command to set your Watson Username and Password."
                               "\nUse one of the following"
                               "\ntemp setup config\ntemp setup envar\n")

        if RunRequest == "temp setup config":
            file = open("config.conf", "w")
            file.write("watson_user=\nwatson_pass=")
        else:
            print("Exiting Program...")
