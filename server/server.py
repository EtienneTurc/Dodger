import socket

UDP_IP = "fe80::9575:8308:9ec9:115"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print("UDP target IP:", UDP_IP)
print("UDP target port:", UDP_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP


for i in range(100):
    sock.sendto(str(i).encode(), (UDP_IP, UDP_PORT))
