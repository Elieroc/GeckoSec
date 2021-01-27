 #!/usr/bin/python3

from Banner import banner
from Pscanner import port_scan
import time
import os


def main():
    os.system('clear')
    banner()
    print("\033[1;36m" + " Welcome to GeckoSec Framework\n")
    choice = inp()
    if choice == "1":
        scan()
    else :
        print("\033[91mBad option !")
        time.sleep(1)
        main()
        os.system('clear')

def inp():
    inp = input("\033[1;37m(\033[91m~\033[1;37m) > \033[1;35m")
    if inp == "menu":
        main()
    if inp == "exit":
        exit(0)
    if inp == "help":
        help()
    # Reset de la couleur
    print('\033[1;37m ')
    return inp

def help():
    print("\033[91mLa page d'aide est en construction !")
    time.sleep(1)
    main()

def scan():
    print("Bienvenue dans la partie Scan !\n")
    print("1) Scan Ninja")
    print("2) Scan des 1024 premiers ports")
    print("3) Scan de tous les ports (pas discret)")
    print("4) Scan d'un seul port\n")
    type = str(inp())
    print("Saisissez l'ip à target :")
    target = str(inp())
    if type == "4":
        print("Saisissez le port à scanner :")
        port = int(inp())
        port_scan(type, target, port)
    port_scan(type, target)
    print("\n")
    inp()

main()
