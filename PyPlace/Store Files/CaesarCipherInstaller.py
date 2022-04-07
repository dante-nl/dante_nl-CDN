#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88


# 🄱🅈 🄳🄰🄽🅃🄴_🄽🄻
# From "100 days of Python" by Angela Yu

# THIS IS ONLY THE INSTALLER!
import re
import sys
import json
import requests
from os.path import exists

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
BaseURL = "https://cdn.dantenl.tk/"

print()
print("————————————————————————————")
print("Welcome to the Caesar Cypher Installer for PyPlace!")
print(f"{bcolors.BOLD}Note:{bcolors.END} This requires an internet connection!")

print(f"{bcolors.INFO}Downloading the main file...")
CaesarCipherMain = requests.get(f"{BaseURL}/PyPlace/Store%20Files/CaesarCipher.py", allow_redirects=True)
if not CaesarCipherMain.ok:
	print(f"{bcolors.FAIL}Error:{bcolors.END} Could not download the Python file! Status code: {CaesarCipherMain.status_code}")
	sys.exit(0)

print(f"{bcolors.OKGREEN}Downloaded the main file!{bcolors.END}")
MainFileName = input("What do you want to call the main file? (leave empty for default) ") or "Caesar Cipher"
InvalidAnswer = True

while InvalidAnswer == True:
	FileExtensionCheck = MainFileName[-3:]
	if FileExtensionCheck == ".py":
		MainFileName = MainFileName.replace(".py", "")
	MainFileName = MainFileName.replace(" ", "-")
	RegExResult = re.search("""\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\+|\=|\[|\{|\]|\}|\||\\|\'|\<|\,|\>|\?|\/|\""|\;|\:|\s""", MainFileName)

	if RegExResult:
		MainFileName = re.sub("""\`|\~|\!|\@|\#|\$|\%|\^|\&|\*|\(|\)|\+|\=|\[|\{|\]|\}|\||\\|\'|\<|\,|\>|\?|\/|\""|\;|\:|\s""", "-", MainFileName)
		print(f"{bcolors.WARNING}WARNING:{bcolors.END} File name contained illegal characters. The file name is now {MainFileName}")
		InvalidAnswer = False
	
	else:
		InvalidAnswer = False
		if exists(f"{MainFileName}.py"):
			print(f"{bcolors.FAIL}Error:{bcolors.END} A file with that name ({MainFileName}.py) already exists!")
			InvalidAnswer = True

print(f"{bcolors.INFO}Installing Python app...{bcolors.END}")
open(f"{MainFileName}.py", 'wb').write(CaesarCipherMain.content)

with open('applications.json') as ApplicationsFile:
	data2 = json.load(ApplicationsFile)
	data2["apps"].update(
	{
		f"{MainFileName}": {
			"name": f"{MainFileName}",
			"file_name": f"{MainFileName}.py",
			"author": "dante_nl",
			"StoreApp": "true"
		}
	})

with open("applications.json", 'w') as json_file:
	json.dump(data2, json_file, indent=4, separators=(',', ': '))

print(f"{bcolors.OKGREEN}Main file installed!{bcolors.END}")


print(f"{bcolors.INFO}Downloading and installing the extra file...")
CaesarCipherExtra = requests.get(f"{BaseURL}/PyPlace/Store%20Files/CaesarCipherArt.py", allow_redirects = True)

if not CaesarCipherExtra.ok:
	print(f"{bcolors.FAIL}Error:{bcolors.END} Could not download the Python file! Status code: {CaesarCipherMain.status_code}")
	sys.exit(0)

open("CaesarCipher_art.py", 'wb').write(CaesarCipherExtra.content)

print(f"{bcolors.OKGREEN}Extra file installed!{bcolors.END}")
print(f"It can now be opened via the \"Open a PyPlace app\" feature on the PyPlace homepage! {bcolors.BOLD}You can delete this file.{bcolors.END} (recommended via the PyPlace settings)")
