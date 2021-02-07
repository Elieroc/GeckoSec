#!/usr/bin/python3

# A pentest framework to facilitate hacker's life (only for ethical hacking !!)
# Leader of project : Elieroc
# Developpers : Elieroc, Stryff3r, Dokanii, Dragorzor
# Start of project : 27/01/2021
# Actual version : ~

from Banner import banner
from Pscanner import port_scan
from Network_scanner import net_scan
import time
import os


def main():
    os.system('clear')
    banner()
    print("\n" + "\033[1;36m" + " Welcome to GeckoSec Framework\n")
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

# Partie scan
def scan():
    print("\nBienvenue dans la partie scan du framework !\n")
    print("1) Scan du réseau")
    print("2) Scanner de port(s)\n")
    type = str(inp())
    if type == "1":
        r_scan()
    if type == "2":
        p_scan()

# Sous-partie : scan réseau
def r_scan():
    os.system("clear")
    print("Bienvenue dans la partie scan de réseau !\n\n")
    print("Saisissez l'ip du réseau :\n")
    net_id = str(inp())
    print("Saisissez la classe du réseau à target :\n")
    print("A : 255.0.0.0")
    print("B : 255.255.0.0")
    print("C : 255.255.255.0\n")
    net_class = str(inp())
    net_scan(net_id, net_class)
    print("\n")
    inp()

# Sous partie : scanner de port(s)
def p_scan():
    os.system("clear")
    print("Bienvenue dans la partie scanner de port(s) !\n")
    print("1) Scan Ninja")
    print("2) Scan des 1024 premiers ports")
    print("3) Scan de tous les ports (pas discret)")
    print("4) Scan d'un seul port\n")
    type = str(inp())
    print("Saisissez l'ip à target :\n")
    target = str(inp())
    if type == "4":
        print("Saisissez le port à scanner :\n")
        port = int(inp())
        port_scan(type, target, port)
    port_scan(type, target)
    print("\n")
    inp()

main()
