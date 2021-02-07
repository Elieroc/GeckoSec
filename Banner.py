#!/usr/bin/python3

# A python Banner printer
# Developed by Elieroc
# Start of project : 27/01/2021
# Actual version : 1.0

import time

# Bannière principale
def banner():
    banner = open('banner.txt', "r")
    banner_lines = banner.readlines()
    banner.close()
    for banner_line in banner_lines:
        string = "\033[1;91m" + banner_line
        print(string.strip())
        time.sleep(0.05)
