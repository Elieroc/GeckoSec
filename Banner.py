import time

# Bannière principale
def banner():
    banner = open('banner.txt', "r")
    banner_lines = banner.readlines()
    banner.close()
    for banner_line in banner_lines:
        print("\033[1;35m" + banner_line)
        time.sleep(0.05)
