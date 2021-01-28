#!/usr/bin/python3

# A python Port-scanner
# Developed by Elieroc
# Start of project : 13/01/2021
# Actual version : 1.0

import socket
import threading

target = '192.168.1.100'

def port_scan(type, target, port=0):
    if type == "1":
        fast(target)
    if type == "2":
        medium(target)
    if type == "3":
        low(target)
    if type == "4":
        if port == 0:
            return 0
        else:
            one(target, port)

def one(target, port):
    print("{*} Début du scan sur " + target + "\n")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = sock.settimeout(0.2)
    if sock.connect_ex((target,port)):
        print("[-] Port " + str(port) + " fermé ! " + "\n")
    else:
        print("[+] Port " + str(port) + " ouvert ! " + "\n")
    sock.close()

    print("{*} Scan terminé !")

def fast(target):
    ports=[21, 22, 23, 53, 80, 443]

    print("{*} Début du scan rapide sur " + target + "\n")

    for port in ports :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = sock.settimeout(0.2)
        if sock.connect_ex((target,port)):
            continue
        else:
            print("[+] Port " + str(port) + " ouvert ! " + "\n")
        sock.close()

    print("{*} Scan terminé !")

def medium(target):
    # Scan des 1024 premiers ports
    print("{*} Début du scan à vitesse moyenne sur " + target + "\n")

    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = sock.settimeout(0.1)
        if sock.connect_ex((target,port)):
            continue
        else:
            print("[+] Port " + str(port) + " ouvert ! " + "\n")
        sock.close()

    print("{*} Scan terminé !")

def low(target):
    # Scan de tous les ports (65536 ports)

    print("{*} Début du scan complet sur " + target + "\n")

    for port in range(1,65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        timeout = sock.settimeout(0.1)
        if sock.connect_ex((target,port)):
            continue
        else:
            print("[+] Port " + str(port) + " ouvert ! " + "\n")
            sock.close()


    print("{*} Scan terminé !")
