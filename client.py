import socket

UDP_IP = "localhost"
UDP_PORT = 8000


class Client():
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET,  # Internet
                                  socket.SOCK_DGRAM)  # UDP

    def connection(self):
        self.sock.sendto("RETRY".encode(), (UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
        return data.decode() != "RESTART"

    def stop(self):
        self.sock.sendto("STOP".encode(), (UDP_IP, UDP_PORT))

    def sendData(self, square, missiles, score):
        message = "SQUARE;" + square.x + ";" + square.y + \
            ";" + square.height + ";" + square.width + ";"
        message += "||"
        for m in missiles:
            message += "MISSILES;" + m.x + ";" + m.y + ";" + m.height + ";" + \
                m.width + ";" + m.direction[0] + ";" + m.direction[1] + ";"

        message += "||"
        message += "SCORE;" + str(score)
        sock.sendto(message.encode(), (UDP_IP, UDP_PORT))
