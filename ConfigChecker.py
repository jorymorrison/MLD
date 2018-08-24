import glob, os

try:
    file = open ("config.conf", "r")
    keys = file.readlines()
    keys = [keys[0][12:].split("\n")[0], keys[1][12:]]
    print("Successfully found Configuration file 'config.conf'")

    if keys[0] == "" or keys[1] == "":
        print("Failed to read variables in config, missing values")
        try:
            keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
            print("Successfully found Environmental Variables")
            if keys[0] == "" or keys[1] == "":
                print("Failed to find value for Environmental Variables")

        except KeyError as er:
            print("Failed to find Environmental Variables")
            print("Please access the config or environmental variables and set the values for Watson Username and Pssword. This program will now exit.")
            print("Exiting Program...")

except IOError as er:
    print("Failed to find file path for 'config.conf'")
    try:
        keys = [os.environ["WATSON_USER"], os.environ["WATSON_PASS"]]
        print("Successfully found Environmental Variables")
        if keys[0] == "" or keys[1] == "":
            print("Failed to find value for Environmental Variables")
    except KeyError as er:
        print("Failed to find Environmental Variables")
        file = open("config.conf", "w")
        file.write("watson_user=\nwatson_pass=")
        print("Successfully generated Configurtion file 'config.conf'")
        print("Please access the config or environmental variables and set the values for Watson Username and Pssword. This program will now exit.")
        print("Exiting Program...")