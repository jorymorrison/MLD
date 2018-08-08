import glob, os

try:
    file = open ("config.conf", "r")
    keys = file.readlines()
    keys = [keys[0][12:].split("\n")[0], keys[1][12:]]
    print(keys)
    if keys[0] == "" or keys[1] == "":
        print ("Config file missing username or password, please set these values.\n Trying environmental variables...")
        try:
            keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
            print(keys)
        except KeyError as er:
            print("Missing environment variables:\nWATSON_USER\nWATSON_PASS\nNeither config file or environmental variables are set, please access 'config.conf' or the environment and set these values.\nExiting Program...")

except IOError as er:
    print("Missing file path 'config.conf'")
    try:
        keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
        print(keys)
    except KeyError as er:
        print("Missing environment variables:\nWATSON_USER\nWATSON_PASS\n")
        print("Neither Config file nor Environmental Variables exist. Generating config.conf...")
        file = open("config.conf", "w")
        file.write("watson_user=\nwatson_pass=")
        print("Please access the config or environmental variables and set the values for Watson Username and Pssword. This program will now exit.")
        print("Exiting Program...")
