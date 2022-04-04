
# ██████╗░██╗░░░██╗██████╗░██╗░░░░░░█████╗░░█████╗░███████╗
# ██╔══██╗╚██╗░██╔╝██╔══██╗██║░░░░░██╔══██╗██╔══██╗██╔════╝
# ██████╔╝░╚████╔╝░██████╔╝██║░░░░░███████║██║░░╚═╝█████╗░░
# ██╔═══╝░░░╚██╔╝░░██╔═══╝░██║░░░░░██╔══██║██║░░██╗██╔══╝░░
# ██║░░░░░░░░██║░░░██║░░░░░███████╗██║░░██║╚█████╔╝███████╗
# ╚═╝░░░░░░░░╚═╝░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚════╝░╚══════╝

# 🄱🅈 🄳🄰🄽🅃🄴_🄽🄻

# Welcome to PyPlace! PyPlace is an easy-to-use Python
# application that allows you to open and install
# various Python applications. PyPlace is designed to
# be as easy to use, so everyone can use it! :D


# ————————————————————————————
# Below you can change more advanced settings,
# that are hard-coded in to PyPlace.
# We only recommend changing these settings
# when you know what you are doing.

# 𝗘𝗻𝗮𝗯𝗹𝗲 𝗼𝗿 𝗱𝗶𝘀𝗮𝗯𝗹𝗲 𝗰𝗵𝗲𝗰𝗸𝗶𝗻𝗴 𝗳𝗼𝗿 𝘂𝗽𝗱𝗮𝘁𝗲𝘀
# Default: True
# Possible options: True, False

# Do you want to check for updates when the
# program is ran? You can always check for
# updates via the advanced options.
import sys
import os
import json
import requests
from os.path import exists
CheckForUpdates = True

# 𝗘𝗻𝗮𝗯𝗹𝗲 𝗼𝗿 𝗱𝗶𝘀𝗮𝗯𝗹𝗲 𝗹𝗼𝗴𝘀
# Default: True
# Possible options: True, False

# Do you want to see exactly what PyPlace
# is doing? This might clutter the output
# with various small things, such as when
# a file is created.
DoNotLogOutput = True

# 𝗖𝘂𝗿𝗿𝗲𝗻𝘁 𝘃𝗲𝗿𝘀𝗶𝗼𝗻
# Default: 0.1 (changes every version)
# Possible options: any number

# This is the version of PyPlace and is
# absolutely not recommended to change,
# except for testing purposes.
Version = 0.1


# ————————————————————————————
# Below this line of text, everything
# that is needed in PyPlace is imported.
# It is absolutely NOT recommended to
# edit this as it can BREAK PyPlace!


# ————————————————————————————
# Below is the main code, it is not
# recommended to edit it, as it might affect
# how well PyPlace runs.

class bcolors:
    LOG = '\033[95m'
    INFO = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


if exists("setup.json") == True:
    with open('setup.json') as SetupFile:
        _data = json.load(SetupFile)
        PyCommand = _data["PythonCommand"]


def log(message):
    if DoNotLogOutput == False:
        print(f"{bcolors.LOG}Log:{bcolors.END} {message}")


def UpdateCheck():
    log("Checking for latest version...")
    response = requests.get("https://cdn.dantenl.tk/PyPlace/version.json")
    if response.status_code != 200:
        print(f"{bcolors.FAIL}Could not check for updates!{bcolors.END}")
        return

    log("Comparing versions...")

    RequestText = response.text
    data = json.loads(RequestText)

    if data["version"] < Version:
        print(f"{bcolors.WARNING}WARNING:{bcolors.END} Your current version seems to be newer than the latest version that is released!")
    elif data["version"] > Version:
        print("————————")
        print(f"{bcolors.BOLD}UPDATE AVAILABLE!{bcolors.END}")
        print(
            f"Your current version ({Version}) is no longer the latest version! The latest one is {data['version']}")
        print(f"""Here are the release notes:
{data["release_notes"]}
        """)
        NotAnswered = True
        while NotAnswered == True:
            Answer = input("Would you like to update right now? (y/n) ")
            Answer = Answer.lower()
            if Answer == "y":
                NotAnswered = False
                print(
                    f"{bcolors.INFO}Downloading latest version of PyPlace...{bcolors.END}")
                log("Retrieving latest version of PyPlace...")
                r = requests.get(
                    "https://cdn.dantenl.tk/PyPlace/PyPlace-Latest.py", allow_redirects=True)
                if not r.ok:
                    print(f"{bcolors.FAIL}Could not get the PyPlace file!")
                    return
                log("Updating main PyPlace file")
                open('PyPlace.py', 'wb').write(r.content)
                print(
                    f"{bcolors.OKGREEN}The latest version of PyPlace is now ready in {bcolors.BOLD}PyPlace.py!{bcolors.END}")
                NotAnswered2 = True
                while NotAnswered2 == True:
                    Answer2 = input("Would you like to run it? (y/n) ")
                    Answer2 = Answer2.lower()
                    if Answer2 == "y":
                        print(
                            f"{bcolors.INFO}Attempting to run PyPlace.py...{bcolors.END}")
                        os.system(f"{PyCommand} PyPlace.py")
                        NotAnswered2 = False
                        sys.exit(1)
                    elif Answer2 == "n":
                        print(
                            f"Continuing with current version. {bcolors.BOLD}NOTE:{bcolors.END} Next time you start PyPlace.py, it will be on the latest version!")
                        NotAnswered2 = False
                        return
                    else:
                        print(
                            f"{bcolors.FAIL}Error:{bcolors.END} I'm not sure what you mean with \"{Answer2}\".")

            elif Answer == "n":
                NotAnswered = False
                print("Update cancelled!")
                return
            else:
                print(
                    f"{bcolors.FAIL}Error:{bcolors.END} I'm not sure what you mean with \"{Answer}\".")


def ExecuteFile():
    with open('applications.json') as AppsFile:
        json_data = json.load(AppsFile)

    ItemCount = 0
    for item in json_data["apps"]:
        ItemCount += 1
        print(f"[{ItemCount}] {json_data['apps'][item]['name']}")

    NumberAppNeeded = input("What number app do you want to open? ")
    ItemCount = 0
    for item in json_data["apps"]:
        ItemCount += 1
        if str(ItemCount) == str(NumberAppNeeded):
            print(
                f"{bcolors.INFO}Attempting to run {json_data['apps'][item]['file_name']}...{bcolors.END}")

            FileExtensionCheck = str(json_data['apps'][item]['file_name'])[-3:]
            if FileExtensionCheck != ".py":
                print(
                    f"{bcolors.FAIL}Error:{bcolors.END} This is not a Python file, and thus can not be executed by PyPlace.")
                return

            elif exists(f"{json_data['apps'][item]['file_name']}") == True:
               os.system(f"{PyCommand} {json_data['apps'][item]['file_name']}")

            else:
                print(
                    f"{bcolors.FAIL}Error:{bcolors.END} {PyCommand} {json_data['apps'][item]['file_name']} does not exist in the current folder.")


def DownloadFile():
    print("""
[1] Link to Python file
[2] Download from PyPlace Store
""")
    NotAnswered4 = True
    while NotAnswered4 == True:
        Answer4 = input("How do you want to add a PyPlace app?")
        if str(Answer4) == "1":
            URLToPythonFile = input(
                "Please enter the direct URL to a Python file: ")


def PyPlaceRegular():
    log("Reading application file...")
    print("What do you want to do?")
    print("""
[1] Open a PyPlace app
[2] Download a PyPlace app
[3] Open settings
""")
    NotAnswered3 = True
    while NotAnswered3 == True:
        Answer3 = input("Enter the number for what you want to do: ")
        if str(Answer3) == "1":
            NotAnswered3 = False
            ExecuteFile()
            return
        else:
            print(
                f"{bcolors.FAIL}Error:{bcolors.END} I'm not sure what you mean with \"{Answer3}\".")


print("————————————————————————————")
print(f"Welcome to {bcolors.BOLD}PyPlace{bcolors.END}!")
print()
print("PyPlace is a Python application that allows you to")
print("to get a simple overview of your other Python")
print("applications, and it also allows you to easily")
print("install new ones!")
print()


log("Checking if setup.json exists...")
if exists("setup.json") == True:
    log("setup.json exists, launching the regular version of PyPlace...")
    if CheckForUpdates != False:
        UpdateCheck()
    PyPlaceRegular()
else:
    log("setup.json does not exist, launching setup...")
    PythonCommand = input(
        "What command do you use to run a Python file in your terminal? ") or "python3"
    print("Leave empty to set it to the default (python3)")
    print(f"{bcolors.BOLD}NOTE: {bcolors.END}You can change this later in the settings.")

    print(f"{bcolors.INFO}Setting up PyPlace...{bcolors.END}")
    SetupDict = {
        "_comment1": "PYPLACE SETUP FILE",
        "_comment2": "This is an important file for PyPlace, because your settings are stored here! It is NOT recommended to delete or edit this file.",
        "SetupVersion": 0.1,
        "PythonCommand": f"{PythonCommand}"
    }

    SetupDictStr = json.dumps(SetupDict)
    with open('setup.json', 'w') as SetupJSON:
        SetupJSON.write(SetupDictStr)
        log("File created: setup.json")

    print(f"{bcolors.OKGREEN}PyPlace is set up!{bcolors.END}")
    # Read content of setup.json key
    # with open('setup.json') as SetupFile:
    #     data = json.load(SetupFile)
    #     print(data["SetupVersion"])
