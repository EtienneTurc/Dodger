import socket
import random
from Display_server import *
from Config_server import *
from Utils_server import *

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))

n = int(input("Number of players: "))

displays = []
for i in range(n):
    displays.append(Display(SCREEN_HEIGHT, SCREEN_WIDTH))

while True:
    restart_retry = False
    addrs = []
    for i in range(n):
        print(i)
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        addrs.append(addr)
        if data.decode() != "RETRY":
            restart_retry = True

    if restart_retry:
        for a in addrs:
            print(a)
            sock.sendto("RESTART".encode(), a)
        continue

    message = str(random.randint(0, 100000))
    for a in addrs:
        print(a)
        sock.sendto(message.encode(), a)

    game_done = 0
    while game_done <= n:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        if data.decode() == 'STOP':
            game_done += 1

        data = data.decode().split("||")
        square = data[0].split(";")[1:]
        square = listToInt(square)
        missiles_str = data[1].split("MISSILES")[1:]
        missiles = []
        for m in missiles_str:
            missiles.append(listToInt(m.split(";")))
        score = int(data[2].split(";")[1])
        displays[addrs.index(addr)].draw(square, missiles, score)
