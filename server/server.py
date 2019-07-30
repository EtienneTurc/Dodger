import socket
import random


UDP_IP = "localhost"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
sock.bind((UDP_IP, UDP_PORT))


n = int(input("Number of players: "))


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

    in_game = True
    while in_game:
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        print(data)
        print(addr)
