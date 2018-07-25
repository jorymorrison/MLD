from pathlib import Path
import json
import glob, os
home = str(Path.home())

try:
    file = open (home + "\\config.txt", "r")

except IOError as er:
    print("Missing file path:\n" + home + "\\config.txt\n")
    try:
        keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
        print(keys)
    except KeyError as er:
        print(
            "Missing evironment variables:\nWATSON_USER\nWATSON_PASS\n")
        SetRunRequest = input ("Please run a set-up command to set your Watson Username and Password."
                               "\nUse:"
                               "\ntemp setup config OR temp setup envar")

        if SetRunRequest == "y" or SetRunRequest == "Y":
            RunRequest = True
        else:
            print("Exiting Program...")
