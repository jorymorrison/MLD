import glob, os

try:
    file = open ("config.conf", "r")
    keys = file.readlines()
    keys = [keys[0][12:].split("\n")[0], keys[1][12:]]
    print(keys)

except IOError as er:
    print("Missing file path 'config.conf' or missing values")
    try:
        keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
        print(keys)
    except KeyError as er:
        print("Missing environment variables:\nWATSON_USER\nWATSON_PASS\n")
        print("Neither Config file nor Environmental Variables exist. Generating config.conf...")
        file = open("config.conf", "w")
        file.write("watson_user=\nwatson_pass=\n")
        print("Please access the config or environmental variables and set the values for Watson Username and Pssword. This program will now exit.")
        print("Exiting Program...")
