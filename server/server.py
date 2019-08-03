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

addrs = []
first_time = True
while True:
    restart_retry = False
    if first_time:
        for i in range(n):
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            print(data)
            addrs.append(addr)
            if data.decode() != "RETRY":
                restart_retry = True
    else:
        ready_addr = []
        while len(ready_addr) < n:
            data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
            if addr not in ready_addr:
                ready_addr.append(addr)
    first_time = False

    if restart_retry:
        for a in addrs:
            print("restart retry", a)
            sock.sendto("RESTART".encode(), a)
        continue

    message = str(random.randint(0, 100000))
    for a in addrs:
        print("seed", a)
        sock.sendto(message.encode(), a)

    game_done = 0
    while game_done < n:
        data, addr = sock.recvfrom(8192)  # buffer size is 1024 bytes
        if data.decode() == "STOP":
            game_done += 1
            continue

        if "SQUARE" not in data.decode() and "MISSILES" not in data.decode() and "SCORE" not in data.decode():
            continue

        data = data.decode().split("||")
        print(data)
        square = data[0].split(";")[1:]
        square = listToInt(square)
        missiles_str = data[1].split("MISSILES")[1:]
        missiles = []
        for m in missiles_str:
            m_str = m.split(";")
            missiles.append(listToInt(m_str[0:4]) + listToFloat(m_str[4:]))
        score = int(data[2].split(";")[1])
        displays[getIndex(addrs, addr)].draw(square, missiles, score)
