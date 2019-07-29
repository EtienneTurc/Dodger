from Config import *


def checkDirection(direction):
    if len(direction) != 2 and (direction[0] > 1 or direction[0] < -1) and (direction[1] > 1 or direction[1] < -1):
        return [0, 0]
    else:
        return direction


def canMove(x_virtual, y_virtual, height, width):
    if (x_virtual < 0 or x_virtual > SCREEN_WIDTH - width) or (y_virtual < 0 or y_virtual > SCREEN_HEIGHT - height):
        return False
    return True


class Square():
    def __init__(self, x_pos, y_pos, h, w, d, s):
        self.x = x_pos  # float
        self.y = y_pos  # float
        self.height = h  # float
        self.width = w  # float
        self.direction = d  # 2 elements => valeurs possibles -1 0 ou 1
        self.speed = s  # float
        self.cd_dash = 0
        self.lives = 3

    def move(self, delta_time):
        x_virtual = self.speed * delta_time * self.direction[0] + self.x
        y_virtual = self.speed * delta_time * self.direction[1] + self.y
        height = self.height
        width = self.width
        if canMove(x_virtual, self.y, height, width):
            self.x = self.speed * delta_time * self.direction[0] + self.x
        else:
            if SCREEN_WIDTH - self.x < self.x:
               self. x = SCREEN_WIDTH - SQUARE_WIDTH
            else:
                self.x = 0
        if canMove(self.x, y_virtual, height, width):
            self.y = self.speed * delta_time * self.direction[1] + self.y
        else:
            if SCREEN_HEIGHT - self.y < self.y:
                self.y = SCREEN_HEIGHT - SQUARE_HEIGHT
            else:
                self.y = 0
        self.cd_dash -= delta_time

    def updateDirection(self, direction):
        self.direction = direction

    def dash(self):
        delta_time = 0.5
        if self.cd_dash <= 0:
            x_virtual = self.speed * delta_time * self.direction[0] + self.x
            y_virtual = self.speed * delta_time * self.direction[1] + self.y
            if x_virtual < 0:
                self.x = 0
            elif x_virtual > SCREEN_WIDTH - self.width:
                self.x = SCREEN_WIDTH - self.width
            else:
                self.x = self.speed * delta_time * self.direction[0] + self.x
            if y_virtual < 0:
                self.y = 0
            elif y_virtual > SCREEN_HEIGHT - self.height:
                self.y = SCREEN_HEIGHT - self.height
            else:
                self.y = self.speed * delta_time * self.direction[1] + self.y
            self.cd_dash = CD_DASH

    def decreaseLife(self):
        self.lives -= 1
