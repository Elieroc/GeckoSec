#!/usr/bin/python3

# A pentest framework to facilitate hacker's life (only for ethical hacking !!)
# Leader of project : Elieroc
# Developpers : Elieroc, Stryff3r, Dokanii, Dragorzor
# Start of project : 27/01/2021
# Actual version : 1.2

# Local Modules
from Banner.banner import *
from Scanning.pscanner import port_scan
from Scanning.network_scanner import net_scan
from Exploitation.Listeners.simple_listener import simple_listener
from Exploitation.Listeners.advanced_listener import main
from Exploitation.Payloads.advanced_reverse_shell import main

# Other Modules
import time
import os


def main():
    os.system('clear')
    banner()
    print("\n" + "\033[1;36m" + " Welcome to GeckoSec Framework\n")
    choice = inp()
    if choice == "1":
        scan_menu()
    if choice == "2":
        exploitation_menu()
    if choice == "3":
        cs_menu()
    if choice == "4":
        se_menu()
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
def scan_menu():

    # Sous-partie 1 : scan réseau
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

    # Sous partie 2 : scanner de port(s)
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

    print("\nBienvenue dans la partie scan du framework !\n")
    print("1) Scan du réseau")
    print("2) Scanner de port(s)\n")
    type = str(inp())
    if type == "1":
        r_scan()
    if type == "2":
        p_scan()

# Partie Exploitation
def exploitation_menu():

    # Sous partie 1 : listeners
    def listener():
        os.system("clear")
        print("Bienvenue dans la partie listeners !\n")
        print("1) Simple Netcat Listener")
        print("2) Advanced Python Listener\n")
        type = str(inp())
        if type == "1":
            print("Saisissez le port d'écoute :")
            port = int(inp())
            simple_listener(port)


    #def payload_generator():
    
    print("\nBienvenue dans la partie Exploitation du framework !\n")
    print("1) Listeners")
    print("2) Payloads generators\n")
    type = str(inp())
    if type == "1":
        listener()
        print("\n")
        inp()

# Partie Social Engineering
def se_menu():

    def phishing():
        os.system('clear')
        os.system('cd SocialPhis/ && sh socialphish.sh')

    print("\nBienvenue dans la partie Social Engineering du framework !\n")
    print("1) Phishing\n")
    type = str(inp())
    if type == "1":
        phishing()
        print("\n")
        inp()


main()
