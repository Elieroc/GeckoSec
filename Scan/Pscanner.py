 #!/usr/bin/python3

import socket
import threading

target = '192.168.1.100'

def port_scan(type, target):
    print('Hummmm')
    if type == "fast" or "1":
        fast(target)
    if type == "medium" or "2":
        medium(target)
    if type == "low" or "3":
        low(target)

def fast(target):
    ports=[21, 22, 23, 53, 80, 443]

    print("{*} Début du scan rapide sur " + target + "\n")

    for port in ports :
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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
        if sock.connect_ex((target,port)):
            continue
        else:
            print("[+] Port " + str(port) + " ouvert ! " + "\n")
            sock.close()


    print("{*} Scan terminé !")
