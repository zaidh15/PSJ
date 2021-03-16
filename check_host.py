import os

hostname = "192.168.0.3" #IP ADDRESS LAPTOP 
response = os.system("ping -n 1 " + hostname)

if response == 0:
    print("Host ", hostname, "Is UP")
else:
    print("Host", hostname, "Is DOWN")