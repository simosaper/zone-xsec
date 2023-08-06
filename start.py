import requests
import re
import os
import time
from colorama import Fore as F, Style
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
os.system('cls' if os.name == 'nt' else 'clear')
yellow = F.LIGHTYELLOW_EX
red = F.LIGHTRED_EX
green = F.LIGHTGREEN_EX
cyan = F.LIGHTCYAN_EX
blue = F.LIGHTBLUE_EX
sb = Style.BRIGHT
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
def logo():
    print(f"""{F.LIGHTCYAN_EX}
         _
   _____(_)___ ___  ____  _________ _____  ___  _____
  / ___/ / __ `__ \/ __ \/ ___/ __ `/ __ \/ _ \/ ___/
 (__  ) / / / / / / /_/ (__  ) /_/ / /_/ /  __/ /
/____/_/_/ /_/ /_/\____/____/\__,_/ .___/\___/_/
                                 /_/                 {F.LIGHTCYAN_EX}
                                                 {F.LIGHTYELLOW_EX} [ ZONE-X GRABBER ]
                                                 {F.LIGHTYELLOW_EX}[  FREE VERSION :0 ]
                                         {F.LIGHTYELLOW_EX}TELEGRAM FOR MORE TOOLS:{F.LIGHTWHITE_EX} https://t.me/simosaper
    """)
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
def zone_x():
    url = 'https://zone-xsec.com/archive/attacker/'
    #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
    print(" ADD NAME ATTACKER YOU WANT GRABB SITES")
    print(" ")
    walker = input(red + sb + '             : NAME : ')
    #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
    link = (url + walker)
    #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
    git = requests.get(link, timeout=5).text
    #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
    hunter = re.findall('<td><im.*\n<.*\n<td>(.*)</td>', git)
    #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
    
    with open('@simosaper11.txt', 'a') as attacker:
        for i in hunter:
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
            a = i.replace('...', '')
            r = a.replace('.c', '.com')
            #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
            o = r.replace('.como' or '.comom', '.com')
            m = o.replace('.comm', '.com')
            #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
            b = m.split('/')[0]
            #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
            print(yellow + sb + '[ # ]', 'http://' + b)
            #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
            attacker.write('http://' + b + '\n')

def main():
    while True:
        print("wait restart.....5")
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
        time.sleep(1)
        print("wait restart.....4")
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
        time.sleep(.5)
        print("wait restart.....3")
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
        time.sleep(.5)
        print("wait restart.....2")
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
        time.sleep(.5) 
        print("wait restart.....1")
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
        os.system('cls' if os.name == 'nt' else 'clear')
        logo()
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
        zone_x()
        #Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^

if __name__ == "__main__":
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^
    main()
#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^#Coder: @simosaper11
#channel: @simosaper
#FREE TOOL !!!
#note: when you show name coder add in source this happen because script kids go sell this tools ^__^