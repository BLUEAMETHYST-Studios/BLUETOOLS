# // BLUETOOLS // by BLUEAMETHYST Studios // SOURCE CODE
import os
import sys
import psutil
import platform
import datetime
import time
import tkinter as tk
import random as rand
import colorama
import openai
from colorama import Fore

#variables
USER = os.getlogin() 
TIME = datetime.datetime.now()
UNIX = time.time()
CPUCORES = psutil.cpu_count()
CPU = platform.processor()
MEM = psutil.virtual_memory().total / int(1024. **3)
COINS = ["HEADS", "TAILS"]
COINFLIP = rand.choice(COINS)
GREETINGLIST = ["Hello! Normally I say Hello World...", "Greetings from a console window!", "Hello (No, there's no World)!", "Hey! Could you help me getting out of that console box?", "DLROW OLLEH = Encrypted Message!", "print('Hello!')"
                , "I said Hello! Am I now an AI?!", "Hello, I'm Blue (daba bee daba die)", "[H]ey! [E]mil [L]ives [L]ike [O]scar. ", "I'm currently printing a string of Hello World" , "Hello, you used the command", "Heyyyyyyyyyyyyyy",
                "Hey! Isn't it weird that a program greets you?", "Hey!\n\nThose are\n\na lot of\n\nlines!\n\nWhoaaaaa!", "Hey or Hello? What do you prefer? And no there's no input, I know it's sad", "Greetings from your console output!"
                ]


#other stuff
colorama.init(autoreset=True)

#startup
os.system("title BLUETOOLS")
print("Welcome to BLUEAMETHYST's BLUETOOLS!")
print("NOTE: You can only use one command per window!")
print('Type "help" to see a list of all commands.\n')

COMMAND=input("> ")

if COMMAND=="info":
    os.system("cls")
    print(Fore.BLUE + "             [ BLUETOOLS ]             ")
    print(Fore.CYAN + "=======================================")
    print("\n")
    print("> Cool tools for you!")
    print("> Made by Simoso68 with <3")
    print("> A project by BLUEAMETHYST Studios")
    print("\n")
    print(Fore.CYAN + "=======================================")
    print("\n")
    print(Fore.RED + "[BT] Closing window in a few seconds.")
    time.sleep(8)
    sys.exit()
#time
elif COMMAND=="time":
    os.system("cls")
    print("Current Time     | " + str(TIME))
    os.system("pause")
    sys.exit()
#unixtime
elif COMMAND=="unixtime":
    os.system("cls")
    print("Current Unixtime | " + str(UNIX))
    os.system("pause")
    sys.exit()
#???
elif COMMAND=="dangerous":
    os.system("cls")
    print("Ohhhhh you found a secret!\nWanna go deeper?")
    #deez
    SECRET_INPUT=input("> ")
    if SECRET_INPUT=="nuts":
        print("hehe funny!")
        os.system("start error")
        print("Was that an error?\n\n\nNo! Intentional of course!")
        os.system("pause")
        sys.exit()
    else:
        print(Fore.RED + "hmm seems like the wrong input!\nLook into the source code and you'll know what todo! >:)\n\n")
        os.system("pause")
        sys.exit()
#download
elif COMMAND=="download":
    os.system("cls")
    print("What do you want to download?")
    print("Type the number to select!")
    print("Options:")
    print("[1] Quickstarter GUI")
    print("[2] Winutils")
    print("[3] Winutils PY")
    print("[4] Microsoft PowerToys")
    print("[5] Discord")
    print("[6] WinAero Tweaker")
    print("[7] Steam")
    print("[8] Epic Games")
    print("[9] Files")
    
    DOWNLOAD=input("> ")
    if DOWNLOAD=="1":
        os.system("start https://github.com/BLUEAMETHYST-Studios/Quick-Starter-GUI/releases/download/utility/QUICK_STARTER_GUI.pyw")
    elif DOWNLOAD=="2":
        os.system("start https://github.com/BLUEAMETHYST-Studios/winutils/releases/download/utility/quick_starter.bat")
    elif DOWNLOAD=="3":
        os.system("start https://github.com/BLUEAMETHYST-Studios/winutils-py/releases/download/utility/quick_starter_dev.py")
    elif DOWNLOAD=="4":
        os.system("start https://github.com/microsoft/PowerToys/releases/download/v0.67.0/PowerToysSetup-0.67.0-arm64.exe")
    elif DOWNLOAD=="5":
        os.system("start https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x86")
    elif DOWNLOAD=="6":
        os.system("start https://winaero.com/downloads/winaerotweaker.zip")
    elif DOWNLOAD=="7":
        os.system("start https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe")
    elif DOWNLOAD=="8":
        os.system("start https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi?trackingId=c80a33f8e3974d6484176ed622d61541")
    elif DOWNLOAD=="9":
        os.system("start https://github.com/files-community/Files/releases/download/v2.4.33/Files.Package_2.4.33.0_x64_ARM64_Sideload.msixbundle")
    else:
        print(Fore.RED + "[BT] Download not supported!\n[BT] Closing window in a moment.")
        time.sleep(5)
        sys.exit()
#createwindow
elif COMMAND=="createwindow":
    os.system("cls")
    print("         This can only be used for VERY BASIC stuff!       ")
    print("===========================================================")
    print("What should be the name of the window?")
    WNAME=input("> ")
    print("What size should the window be? (Don't forget the 'x' !)")
    print("Example: 1000x1000")
    WSIZE=input("> ")
    print("What text should be in the window?")
    WTEXT=input("> ")
    print("How big should the text be? (In pixels)")
    WFONTSIZE=input("> ")
    
    window = tk.Tk()
    window.title(WNAME)
    window.geometry(WSIZE)
    text1 = tk.Label(window, text=WTEXT, font=("Arial", WFONTSIZE))
    text1.pack(padx=20, pady=20)

    window.mainloop()
#current version of java
elif COMMAND=="ver-java":
    os.system("cls")
    os.system("java -version")
    os.system("pause")
    sys.exit()
#current version of python
elif COMMAND=="ver-py":
    os.system("cls")
    os.system("py --version")
    os.system("pause")
    sys.exit()
#send a cmd command
elif COMMAND=="cmd":
    os.system("cls")
    print("Enter a command, that should be executed by the windows command prompt.")
    CMD=input("> ")
    os.system(CMD)
    os.system("pause")
    sys.exit()
#who am i?
elif COMMAND=="getname":
    os.system("cls")
    print("Current user     | " + str(USER))
    os.system("pause")
    sys.exit()
#cpu information
elif COMMAND=="cpu":
    os.system("cls")
    print("Processor        | " + str(CPU)) 
    print("Number of cores  | " + str(CPUCORES))
    os.system("pause")
    sys.exit()
#memory information 
elif COMMAND=="memory":
    os.system("cls")
    print("Total memory     | " + str(MEM) + " GB")
    os.system("pause")
    sys.exit()
#coinflip
elif COMMAND=="coinflip":
    os.system("cls")
    print(Fore.GREEN + "\n============================================================================================================")
    print(Fore.GREEN + "\nThe coin landed on the " + Fore.CYAN + COINFLIP + Fore.GREEN + " side!\n")
    print(Fore.GREEN + "============================================================================================================\n")
    os.system("pause")
    sys.exit()
#random number generator
elif COMMAND=="rng":
    os.system("cls")
    print("Between which numbers should it be?")
    FIRNUM = input("First Number > ")
    SECNUM = input("Second Number > ")
    RANDNUM = rand.uniform(float(FIRNUM), float(SECNUM))
    print(RANDNUM)
    print("\n")
    os.system("pause")
    sys.exit()
#random integer generator
elif COMMAND=="rng-int":
    os.system("cls")
    print("Between which integers should it be?")
    FIRINT = input("First Integer > ")
    SECINT = input("Second Integer > ")
    RANDINT = rand.randint(int(FIRINT), int(SECINT))
    print(RANDINT)
    os.system("pause")
    sys.exit()
#random greeting
elif COMMAND=="greeting":
    os.system("cls")
    GREETING = rand.choice(GREETINGLIST)
    print(GREETING)
    os.system("pause")
    sys.exit()
#random word
elif COMMAND=="rand-word":
    os.system("cls")
    RANDWORDLIST = ["craven", "meat", "snow", "agonizing", "phobic", "stem", "jumbled", "eight", "bit", "bubble", "aboard", "bright", "yummy", "tub", "useful", "eatable", "innocent", "spray", "rat", "high-pitched",
                    "search", "brush", "bucket", "rate", "foregoing", "fool", "utopian", "statement", "kettle", "donkey", "continue", "high", "offbeat", "pump", "say", "elegant", "ski", "tart", "cat", "quartz",
                    "unbecoming", "psychedelic", "draconian", "pale", "cowardly", "fresh", "homeless", "beam", "rejoice", "unnatural", "periodic", "finicky", "frail", "wonderful", "dull", "public", "carry", "deafening", "whip", "theory",
                    "intelligent", "earn", "glistening", "trace", "concentrate", "ready", "disapprove", "class", "two", "absurd", "amuse", "spring", "reflective", "paste", "laugh", "tin", "minute", "poison", "same", "excite",
                    "minor", "fox", "unable", "strengthen", "whole", "hunt", "instrument", "notice", "nervous", "sudden", "future", "automatic", "therapeutic", "wrist", "bridge", "perpetual", "club", "mug", "delicious", "massive"
                    ]
    RANDWORD = rand.choice(RANDWORDLIST)
    print(RANDWORD)
    RANDWORDCLOSE = input("Enter anything to close > ")
    sys.exit()
#predict game
elif COMMAND=="predict":
    os.system("cls")
    print(Fore.CYAN + "You'll need to predict a random number, which can be 1 through 10!\nAre you ready?")
    PREDICTGUESS = input("YOUR NUMBER GUESS > ")
    PREDICTINT = rand.randint(1, 10)
    if int(PREDICTGUESS) == PREDICTINT:
        print(Fore.GREEN + "Your guess was right!\nThe number was: " + Fore.CYAN + str(PREDICTINT) + Fore.GREEN + " !")
        print("\n" + Fore.RED + "This window will automatically be closed in a moment!")
        time.sleep(7)
        sys.exit()
    else:
        print(Fore.RED + "Your guess was wrong!\nThe correct number was: " + Fore.CYAN + str(PREDICTINT) + Fore.RED + " !")
        print("\n" + Fore.RED + "This window will automatically be closed in a moment!")
        time.sleep(7)
        sys.exit()
#chatgpt
elif COMMAND=="chatgpt":
    os.system("cls")
    print("Due to this using the OpenAI API, you'll need to enter your API Key!")
    print("If you enter an invalid API Key this won't work!")
    APIKEY = input("API Key > ")
    
    openai.api_key = APIKEY
    GPT = input("Ask ChatGPT > ")
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt='ChatGPT: ' + GPT,
            max_tokens=2048,
            n=1,
            stop=None, 
            temperature=0.5,
        ).choices[0].text
        
    print(Fore.CYAN + response)
        
    time.sleep(3)
    print("\n\n")
    GPTCLOSE = input("Enter anything to close > ")
    sys.exit()
#help
elif COMMAND=="help":
    os.system("cls")
    print("========================================================================================================================\n")
    print("help - Shows you a list of commands.")
    print("info - Shows a little bit of info about this program.")
    print("time - Shows the current time.")
    print("unixtime - Shows the current unixtime.")
    print("download - Can download a few currently supported programs.")
    print("createwindow - Allows you to create your own custom window. (Very limited!)")
    print("ver-java - Gets the current version of Java on your system.")
    print("ver-py - Gets the current version of Python on your system.")
    print("cmd - Allows you to use nearly every CMD-Command.")
    print("getname - Shows your current username.")
    print("cpu - Shows the brand name of your processor and the amount of cores.")
    print("memory - Shows your current memory in gigabytes.")
    print("coinflip - Flips a coin and has a 50/50 chance of landing on HEADS or TAILS.")
    print("rng - [R]andom [N]umber [G]enerator.")
    print("rng-int - Generates a random integer (Not a decimal!)")
    print("rand-word - Chooses a random word from a 100-Word list.")
    print("greeting - Greets you with a random greeting.")
    print("predict - Allows you to play a little game, in which you need to predict a number!")
    print("chatgpt - Ask ChatGPT! You'll need an API Key to do that!")
    print("\n========================================================================================================================\n")
    print(Fore.RED + "\n[BT] You'll need to restart the program to send another command!")
    os.system("pause")
    sys.exit()
#unknown command sent
else:
    os.system("cls")
    print(Fore.RED + "[BT] Unknown command!\n[BT] Maybe typed wrong?\n[BT] You'll need to restart the program!")
    os.system("pause")
    sys.exit()



#END OF CODE // MADE BY BLUEAMETHYST Studios




#Hello I'm under the code, please help me.