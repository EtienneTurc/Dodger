import socket

UDP_IP = "localhost"
UDP_PORT = 8000


class Client():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP

    def connect(self):
        self.sock.sendto("RETRY".encode(), (UDP_IP, UDP_PORT))
        data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
        return data.decode()

    def stop(self):
        self.sock.sendto("STOP".encode(), (UDP_IP, UDP_PORT))

    def sendData(self, square, missiles, score):
        message = "SQUARE;" + str(square.x) + ";" + str(square.y) + \
            ";" + str(square.height) + ";" + str(square.width) + ";"
        message += "||"
        for m in missiles:
            message += "MISSILES;" + str(m.x) + ";" + str(m.y) + ";" + str(m.height) + ";" + \
                str(m.width) + ";" + \
                str(m.direction[0]) + ";" + str(m.direction[1]) + ";"

        message += "||"
        message += "SCORE;" + str(score)
        self.sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
