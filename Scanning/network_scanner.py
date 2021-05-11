#!/usr/bin/python3

# A Network-scanner
# Developed by Elieroc
# Start of project : 28/01/2021
# Actual version : 1.1

import os
import socket
import netifaces
import subprocess
import sys
from collections import Counter

def get_ip():
    # Code obtenu sur StackOverflow pour obtenir une ip
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Ici on essaye de se connecter à une IP
    # ici l'ip du réseau pour ne pas envoyer un paquet indiscret
    # pour pouvoir récupérer notre ip
    try:
        # doesn't even have to be reachable
        s.connect(('192.168.1.0', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

def ping(host):
    command = "import os;os.system('ping -c 1 " + host + "')"

    try:
        result = subprocess.run(
            [sys.executable, "-c", command], capture_output=True, text=True, timeout=0.5
        )

        print("[+] " + host )
        return host

    except:
        # Si il y a une erreur (si l'ip scanné n'est pas active) on ne fait rien
        null = 0

def net_scan(net_id, mask):

    # On met la classe (a, b ou c) en maj pour supporter les entrées en majuscules
    mask_type = mask.upper()
    byte = 0

    # Classe C
    if mask_type == "C":
        for character in range (len(net_id)):
            if byte != 3:
                if net_id[character] == ".":
                    byte = byte + 1
            else:
                # On enlève le "0" (le dernier octet)
                # net_id_w car c'est l'ip réseau sans le dernier octet (w comme without)
                net_id_w = len(net_id) - 1
                # Début de l'ip / start ip
                st_ip = net_id
                st_ip = st_ip[:net_id_w]

                # Résultat bruteforce
                r_bf = bruteforce(st_ip, mask_type, 0)

                for ip in r_bf:
                    ping(ip)
    # Classe B
    if mask_type == "B":
        # On capture le 3ème octet car il y a 2 "255"
        # Result of byte_capture function
        r_bc = byte_capture(net_id, 3)

        # Last byte net id / Dernier octet de l'ip du réseau
        l_byte_ni = r_bc[0]
        # Position in ip
        p_in_ip = r_bc[1]

        for character in range (len(net_id)):
            if byte != 2:
                if net_id[character] == ".":
                    byte = byte + 1
            else:
                # On enlève le "0" (du troisième octet)

                net_id_w = len(net_id) - 1
                final = 0
                final = net_id[:net_id_w]

        # On parcours jusqu'à l'octet en question
        byte = 0
        # Début de l'ip
        st_ip = ""
        for character in range (len(final)):
            if byte < 2:
                if net_id[character] == ".":
                    byte = byte + 1
                st_ip = st_ip + str(net_id[character])


        # Résultat bruteforce
        r_bf = bruteforce(st_ip, mask_type, int(l_byte_ni))

        for ip in r_bf:
            ping(ip)

    # Classe A
    if mask_type == "A":
        # On capture le 2ème octet car il y a 1 "255"
        # Result of byte_capture function
        r_bc = byte_capture(net_id, 2)

        # Last byte net id / Dernier octet de l'ip du réseau
        l_byte_ni = r_bc[0]
        # Position in ip
        p_in_ip = r_bc[1]

        for character in range (len(net_id)):
            if byte != 2:
                if net_id[character] == ".":
                    byte = byte + 1
            else:
                # On enlève le "0" (du deuxième octet)

                net_id_w = len(net_id) - 1
                final = 0
                final = net_id[:net_id_w]

        # On parcours jusqu'à l'octet en question
        byte = 0
        # Début de l'ip
        st_ip = ""
        for character in range (len(final)):
            if byte < 1:
                if net_id[character] == ".":
                    byte = byte + 1
                st_ip = st_ip + str(net_id[character])


        # Résultat bruteforce
        r_bf = bruteforce(st_ip, mask_type, int(l_byte_ni))

        for ip in r_bf:
            ping(ip)


def bruteforce(st_ip, mask_type, i):
    # i correspond au nombre de départ du bruteforce
    # Ici on l'incrémente pour qu'il ne scan pas l'ip réseau
    i = i+1
    # Liste des Ip qu'il faudra scanner
    list_ip_to_test = []

    if mask_type == "A":
        # Deuxième compteur (pour l'avant dernier octet)
        i2 = 0
        # Troisième compteur (pour le dernier octet)
        i3 = 1
        while i <= 254:
            while i2 <= 254:
                while i3 <= 254:
                    # Ip à tester
                    ip_to_test = st_ip + str(i) + "." + str(i2) + "." + str(i3)
                    list_ip_to_test.append(ip_to_test)
                    i3 = i3+1
                # On remet la valeur de notre dernier octet à 1
                i3 = 1

                i2 = i2 + 1
            # On remet la valeur de notre avant-dernier octet à 1
            i2 = 1

            i = i+1
        return list_ip_to_test

    if mask_type == "B":
        # Deuxième compteur (pour le dernier octet)
        i2 = 1
        while i <= 254:
            while i2 <= 254:
                # Ip à tester
                ip_to_test = st_ip + str(i) + "." + str(i2)
                list_ip_to_test.append(ip_to_test)
                i2 = i2+1
            # On remet la valeur de notre dernier octet à 1
            i2 = 1

            i = i+1
        return list_ip_to_test

    if mask_type == "C":
        while i <= 254:
            # Ip à tester
            ip_to_test = st_ip + str(i)
            list_ip_to_test.append(ip_to_test)
            i = i+1
        return list_ip_to_test

def byte_capture(ip, byte_to_cap):
    # Le deuxième argument de la fonction est l'octet à récupérer
    # Permet d'obtenir la longueur sans l'octet demandé (mais avec le ".")
    byte = 0
    lenght_ip1 = 0
    for character in range (len(ip)):
        if byte != byte_to_cap - 1:
            if ip[character] == ".":
                byte = byte + 1
                lenght_ip1 = lenght_ip1 + 1
            else:
                lenght_ip1 = lenght_ip1 + 1

    # Permet d'obtenir la longueur avec l'octet demandé (avec le ".")
    byte = 0
    lenght_ip2 = 0
    for character in range (len(ip)):
        if byte != byte_to_cap:
            if ip[character] == ".":
                byte = byte + 1
                lenght_ip2 = lenght_ip2 + 1
            else:
                lenght_ip2 = lenght_ip2 + 1
    #Enlève le "."
    lenght_ip2 = lenght_ip2-1

    # Calcule de la différence pour extraire l'octet réclamé
    byte_captured = ""
    i = lenght_ip1
    i2 = 0
    diff = lenght_ip2-lenght_ip1
    while i2 < diff:
        byte_captured = byte_captured + str(ip[i])
        i = i + 1
        i2 = i2 + 1
    # Le résultat est un tableau où est stocké la valeur de l'octet capturé ainsi que sa position dans l'ip
    return [byte_captured, lenght_ip1+1]
