from colorama import init,Fore,Style
from tkinter import filedialog
import random
import json
import time
import phonenumbers
from phonenumbers import carrier
from phonenumbers.phonenumberutil import number_type
import random,time,os,sys
from datetime import datetime   


init()

if not os.path.exists("Results" + os.sep + "Carrier"):
    os.makedirs("Results" + os.sep + "Carrier")

black = Fore.LIGHTBLACK_EX
blue = Fore.GREEN
green = Fore.LIGHTGREEN_EX
reset = Style.RESET_ALL
red = Fore.RED
white = Fore.LIGHTWHITE_EX
black = Fore.LIGHTBLACK_EX
green = Fore.LIGHTGREEN_EX


expiry_date = datetime(2025, 11, 20)
if datetime.now() >= expiry_date:
    print(f"{Fore.RED}[X] TRAIL DONE ! PM OWNER TO RENEW: t.me/simosaper11{reset}")
    time.sleep(10000)
    sys.exit(0)

def Banner():
        clear = "\x1b[0m"
        colors = [ 36,33,34,35,37,36]
        x = """
                                                                                          (api update)
        _            _    _           _                            _           _         /
 | |   | |          | |  | |         | |                          | |         (_)       /
 | |__ | | __ _  ___| | _| |__   __ _| |_    ___  __ _ _   _ _ __ | |_  __   ___ _ __  /
 | '_ \| |/ _` |/ __| |/ / '_ \ / _` | __|  / _ \/ _` | | | | '_ \| __| \ \ / / | '_ \ 
 | |_) | | (_| | (__|   <| | | | (_| | |_  |  __/ (_| | |_| | |_) | |_   \ V /| | |_) |
 |_.__/|_|\__,_|\___|_|\_\_| |_|\__,_|\__|  \___|\__, |\__, | .__/ \__|   \_/ |_| .__/ 
                         (priv script)            __/ | __/ | |                 | |    
                                                 |___/ |___/|_|                 |_|    

                              [PH-VALIDATOR]
                           CODER  [ M@hmEd m@dy ]
                           Telegram: @simosaper11

"""
        for N, line in enumerate(x.split("\n")):
            sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
            time.sleep(0.05)
Banner()            

def LoadFile(title):
        print(f"                {black}[{blue}~{black}]{blue} {title}: ",end='')
        input()
        filepath = filedialog.askopenfilename(title=title)
        badlist = []
        try:
            lines = open(filepath,errors="ignore").readlines()
            for line in lines:
                line = line.replace("+","")
                badlist.append(line.split("\n")[0])
        except Exception as e:
            return LoadFile(title)
        FinalList = dict.fromkeys(badlist)
        print(f"                {black}[{blue}~{black}]{blue} Loaded {len(FinalList)} | Removed: {len(badlist)-len(FinalList)} duplicates.\n")
        return FinalList

def HLRUSA():
        module = "HLR Lookup USA Only"
        print(f"                {black}({blue}~{black}) Gettinbg DB....")
        AREACODES_DB = json.loads(open("AREACODES.json","r").read())
        PREFIXESDATA_DB = json.loads(open("PREFIXEX_DATA.json","r").read())
        numbers = LoadFile("Load Numbers")
        for number in numbers:
            try:
                tempnumber = number
                if tempnumber.startswith("1"):
                    tempnumber = tempnumber[1:]
                parse = phonenumbers.parse(tempnumber,"US")
                if phonenumbers.is_valid_number(parse):
                    if carrier._is_mobile(number_type(parse)):
                        PREFIXES = AREACODES_DB['list'][str(tempnumber[:3])]
                        Carrier = "Nothing"
                        for PREFIX in PREFIXES:
                            if PREFIX[0]==int(tempnumber[3:6]):
                                Carrier = PREFIXESDATA_DB['companies'][PREFIX[4]]
                                break
                            else: continue
                        if Carrier!="" and Carrier!="Nothing":
                            print(f"{Fore.LIGHTGREEN_EX}(+) {number} | Carrier: {Carrier}")
                            file = open(f"Results{os.sep}Carrier{os.sep}{Carrier}.txt","a")
                            file.write('+'+number+"\n")
                            file.close()
                        else:
                            pass
                        
                elif phonenumbers.is_valid_number(parse) == False:
                    pass
                else:
                    pass
            except Exception as e:
                pass
HLRUSA()
