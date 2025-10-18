try:
    from scapy.all import *
except ModuleNotFoundError:
    import subprocess
    subprocess.call("pip install scapy", shell=True)
    from scapy.all import *
    
try:
    import pyfiglet
except ModuleNotFoundError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyfiglet"])
    import pyfiglet

print(pyfiglet.figlet_format("ARP SCANNER \n ~ By Ambika"))

from scapy.all import get_if_list
print("Available interfaces:", get_if_list())

interface = input("Enter Your Interface eth0/wlan0: ")  
ip_range = input("Enter Your IP range , 10.10.X.X/24: ")  
broadcastMac = input("Enter Your IP range , ff:ff:ff:ff:ff:ff(Optional)")

packet = Ether(dst=broadcastMac) / ARP(pdst=ip_range)

ans, unans = srp(packet, timeout=2, iface=interface, inter=0.1)

for send, receive in ans:
    print(receive.sprintf(r"%Ether.src% - %ARP.psrc%"))
