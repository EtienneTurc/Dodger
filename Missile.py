from math import *
import random
from Config import *


def norm(d):
    n = sqrt(d[0] ** 2 + d[1] ** 2)
    n_d = [d[0]/n, d[1] / n]
    return n_d


def initPosition():
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    return x, y


class Missile():
    def __init__(self, h, w, d, s):
        self.x, self.y = initPosition()
        # self.x = x_pos  # float
        # self.y = y_pos  # float
        self.height = h  # float
        self.width = w  # float
        self.direction = norm(d)  # 2 elements normés entre -1 et 1
        self.speed = s

    def move(self):
        self.x = self.speed * self.direction[0] + self.x
        self.y = self.speed * self.direction[1] + self.y
