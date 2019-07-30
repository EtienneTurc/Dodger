import socket

UDP_IP = "localhost"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP

# while True:
sock.sendto("RETRY".encode(), (UDP_IP, UDP_PORT))
# sock.sendto("RESTART".encode(), (UDP_IP, UDP_PORT))
data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes

print(data.decode())
print(addr)
