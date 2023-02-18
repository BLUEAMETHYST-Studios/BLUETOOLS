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
BTVERSION = "0.0.4"
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
#cleanup
os.system("cls")

#startup 
os.system("title BLUETOOLS")

print(Fore.CYAN + "Welcome to BLUEAMETHYST's BLUETOOLS!")
print(Fore.CYAN  + 'Type "help" to see a list of all commands.\n')

#other stuff
while True:
    colorama.init(autoreset=True)
    

    COMMAND=input(Fore.LIGHTBLUE_EX + "> " + Fore.CYAN)

#info
    if COMMAND=="info":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "                    [ BLUETOOLS ]             ")
        print(Fore.CYAN + "======================================================")
        print("\n")
        print("> Bluetools offers great tools for you!")
        print("> Current version: " + BTVERSION)
        print("> Made by Simoso68 with <3")
        print("> A project by BLUEAMETHYST Studios")
        print("\n")
        print(Fore.CYAN + "======================================================")
        print("\n")
#time
    elif COMMAND=="time":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Current Time     | " + Fore.CYAN + str(TIME)) 
#unixtime
    elif COMMAND=="unixtime":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Current Unixtime | " + Fore.CYAN  + str(UNIX))
#download
    elif COMMAND=="download":
        os.system("cls")
        print(Fore.CYAN + "What do you want to download?")
        print(Fore.CYAN + "Type the number to select!")
        print(Fore.CYAN + "Options:")
        print(Fore.LIGHTBLUE_EX + "[1] Quickstarter GUI")
        print(Fore.LIGHTBLUE_EX + "[2] Winutils")
        print(Fore.LIGHTBLUE_EX + "[3] Winutils PY")
        print(Fore.LIGHTBLUE_EX + "[4] Microsoft PowerToys")
        print(Fore.LIGHTBLUE_EX + "[5] Discord")
        print(Fore.LIGHTBLUE_EX + "[6] WinAero Tweaker")
        print(Fore.LIGHTBLUE_EX + "[7] Steam")
        print(Fore.LIGHTBLUE_EX + "[8] Epic Games")
        print(Fore.LIGHTBLUE_EX + "[9] Files")
    
        DOWNLOAD=input(Fore.LIGHTBLUE_EX + "> " + Fore.CYAN)
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
            print(Fore.RED + "[BT] Download not supported!")

#createwindow
    elif COMMAND=="createwindow":
        os.system("cls")
        print(Fore.CYAN + "         This can only be used for VERY BASIC stuff!       ")
        print(Fore.LIGHTBLUE_EX + "===========================================================")
        print(Fore.LIGHTBLUE_EX + "What should be the name of the window?")
        WNAME=input(Fore.LIGHTBLUE_EX + "> " + Fore.CYAN)
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "What size should the window be?\nDon't forget the " + '"x" !')
        print(Fore.LIGHTBLUE_EX + "Example: 1000x1000")
        WSIZE=input(Fore.LIGHTBLUE_EX + "> " + Fore.CYAN)
        os.system("cls")
        try:
            w, h = WSIZE.split('x')
            w = int(w)
            h = int(h)
        except ValueError:
            os.system("cls")
            print(Fore.RED + "[BT] The input " + Fore.CYAN + WSIZE + Fore.RED + " isn't a valid window size!")
            print(Fore.RED + "[BT] Please follow the format of the example (Example: 1000x1000)!")
        else:
            
            print(Fore.LIGHTBLUE_EX + "What text should be in the window?")
            WTEXT=input(Fore.LIGHTBLUE_EX + "> " + Fore.CYAN)
            os.system("cls")
            print(Fore.LIGHTBLUE_EX + "How big should the text be? (In pixels)")
            WFONTSIZE=input(Fore.LIGHTBLUE_EX + "> " + Fore.CYAN)
            os.system("cls")
            try:
                WFONTSIZE = int(WFONTSIZE)
            except ValueError:
                os.system("cls")
                print(Fore.RED + "[BT] Font size must be an integer!")
                print(Fore.RED + "[BT] The input " + Fore.CYAN + WFONTSIZE + Fore.RED + " isn't a valid fontsize!")
            else:
                print(Fore.CYAN + "[BT] Window Title: " + WNAME )
                print(Fore.CYAN + "[BT] Window Width: " + str(w) )
                print(Fore.CYAN + "[BT] Window Height: " + str(h) )
                print(Fore.CYAN + "[BT] Window Text: " + WTEXT )
                print(Fore.CYAN + "[BT] Window Text Fontsize: " + str(WFONTSIZE) )
                window = tk.Tk()
                window.title(WNAME)
                window.geometry(f"{w}x{h}")
                text1 = tk.Label(window, text=WTEXT, font=("Arial", WFONTSIZE))
                text1.pack(padx=20, pady=20)

                window.mainloop()
#current version of java
    elif COMMAND=="ver-java":
        os.system("cls")
        os.system("java -version")
#current version of python
    elif COMMAND=="ver-py":
        os.system("cls")
        os.system("py --version")
#send a cmd command
    elif COMMAND=="cmd":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Enter a command, that should be executed by the windows command prompt.")
        CMD=input(Fore.LIGHTBLUE_EX + "> " + Fore.CYAN)
        os.system(CMD)
        os.system("cls")
#who am i?
    elif COMMAND=="getname":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Current user     | " + Fore.CYAN + str(USER))
#cpu information
    elif COMMAND=="cpu":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Processor        | " + Fore.CYAN + str(CPU)) 
        print(Fore.LIGHTBLUE_EX + "Number of cores  | " + Fore.CYAN + str(CPUCORES))
#memory information 
    elif COMMAND=="memory":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Total memory     | " + Fore.CYAN + str(MEM) + " GB")
#coinflip
    elif COMMAND=="coinflip":
        os.system("cls")
        print(Fore.GREEN + "\n============================================================================================================")
        print(Fore.GREEN + "\nThe coin landed on the " + Fore.CYAN + COINFLIP + Fore.GREEN + " side!\n")
        print(Fore.GREEN + "============================================================================================================\n")
#random number generator
    elif COMMAND=="rng":
        os.system("cls")
        print("Between which numbers should it be?")
        FIRNUM = input(Fore.LIGHTBLUE_EX + "First Number > " + Fore.CYAN)
        SECNUM = input(Fore.LIGHTBLUE_EX + "Second Number > " + Fore.CYAN)
        RANDNUM = rand.uniform(float(FIRNUM), float(SECNUM))
        print(RANDNUM)
        print("\n")
#random integer generator
    elif COMMAND=="rng-int":
        os.system("cls")
        print("Between which integers should it be?")
        FIRINT = input(Fore.LIGHTBLUE_EX + "First Integer > " + Fore.CYAN)
        SECINT = input(Fore.LIGHTBLUE_EX + "Second Integer > " + Fore.CYAN)
        RANDINT = rand.randint(int(FIRINT), int(SECINT))
        print(RANDINT)
#random greeting
    elif COMMAND=="greeting":
        os.system("cls")
        GREETING = rand.choice(GREETINGLIST)
        print(GREETING)
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
        print(Fore.CYAN + RANDWORD)
#predict game
    elif COMMAND=="predict":
        os.system("cls")
        print(Fore.CYAN + "You'll need to predict a random number, which can be 1 through 10!\nAre you ready?")
        PREDICTGUESS = input("YOUR NUMBER GUESS > ")
        PREDICTINT = rand.randint(1, 10)
        if int(PREDICTGUESS) == PREDICTINT:
            print(Fore.GREEN + "Your guess was right!\nThe number was: " + Fore.CYAN + str(PREDICTINT) + Fore.GREEN + " !") 

        else:
            print(Fore.RED + "Your guess was wrong!\nThe correct number was: " + Fore.CYAN + str(PREDICTINT) + Fore.RED + " !")

#chatgpt
    elif COMMAND=="chatgpt":
        os.system("cls")
        print(Fore.LIGHTBLUE_EX + "Please enter your OpenAI API Key!")
        print(Fore.LIGHTBLUE_EX + "If you don't have one, create one to use this tool!")
        try:
            openai.api_key = input(Fore.LIGHTBLUE_EX + "API Key > " + Fore.CYAN)
            os.system("cls")
            print(Fore.LIGHTBLUE_EX + "[BT] Sending request to OpenAI, to check if the API Key is valid...")
            openai.Completion.create(
                engine="text-davinci-003",
                prompt='ChatGPT: Hello!',
                max_tokens=2048,
                n=1,
               stop=None,
               temperature=0.5,
            )
            os.system("cls")
        except Exception as error:
            os.system("cls")
            print(Fore.RED + "[BT] Invalid OpenAI API Key!")
        else:
            while True:
                GPT = input(Fore.LIGHTBLUE_EX + "Talk to ChatGPT > " + Fore.CYAN)
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=GPT,
                    max_tokens=2048,
                    n=1,
                    stop=None, 
                    temperature=0.5,
                ).choices[0].text

                print(Fore.CYAN + response)
                print("\n")
                input(Fore.LIGHTBLUE_EX + 'Press ENTER to talk again to ChatGPT > ')
                

    elif COMMAND=="close":
        sys.exit()
#help
    elif COMMAND=="help":
        os.system("cls")
        print(Fore.CYAN + "========================================================================================================================\n")
        print(Fore.LIGHTBLUE_EX + "help - Shows you a list of commands.")
        print(Fore.LIGHTBLUE_EX + "info - Shows a little bit of info about this program.")
        print(Fore.LIGHTBLUE_EX + "time - Shows the current time.")
        print(Fore.LIGHTBLUE_EX + "unixtime - Shows the current unixtime.")
        print(Fore.LIGHTBLUE_EX + "download - Can download a few currently supported programs.")
        print(Fore.LIGHTBLUE_EX + "createwindow - Allows you to create your own custom window. (Very limited!)")
        print(Fore.LIGHTBLUE_EX + "ver-java - Gets the current version of Java on your system.")
        print(Fore.LIGHTBLUE_EX + "ver-py - Gets the current version of Python on your system.")
        print(Fore.LIGHTBLUE_EX + "cmd - Allows you to use nearly every CMD-Command.")
        print(Fore.LIGHTBLUE_EX + "getname - Shows your current username.")
        print(Fore.LIGHTBLUE_EX + "cpu - Shows the brand name of your processor and the amount of cores.")
        print(Fore.LIGHTBLUE_EX + "memory - Shows your current memory in gigabytes.")
        print(Fore.LIGHTBLUE_EX + "coinflip - Flips a coin and has a 50/50 chance of landing on HEADS or TAILS.")
        print(Fore.LIGHTBLUE_EX + "rng - [R]andom [N]umber [G]enerator.")
        print(Fore.LIGHTBLUE_EX + "rng-int - Generates a random integer (Not a decimal!)")
        print(Fore.LIGHTBLUE_EX + "rand-word - Chooses a random word from a 100-Word list.")
        print(Fore.LIGHTBLUE_EX + "greeting - Greets you with a random greeting.")
        print(Fore.LIGHTBLUE_EX + "predict - Allows you to play a little game, in which you need to predict a number!")
        print(Fore.LIGHTBLUE_EX + "chatgpt - Ask ChatGPT! You'll need an API Key to do that!")
        print(Fore.LIGHTBLUE_EX + "close - Exits the window.")
        print(Fore.CYAN + "\n========================================================================================================================\n")
#unknown command sent
    else:
        os.system("cls")
        print(Fore.RED + "[BT] Command " + Fore.CYAN +  COMMAND +  Fore.RED + " is not available!")
        print(Fore.RED + '[BT] Type "help" to list all commands.')
#loop end
    print("\n\n")
    input(Fore.LIGHTBLUE_EX + "Press ENTER to continue > ")
    os.system("cls")


#END OF CODE // MADE BY BLUEAMETHYST Studios


#Hello I'm under the code, please help me.