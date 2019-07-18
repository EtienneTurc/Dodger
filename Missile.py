from math import *
import random
from Config import *
import numpy as np


def norm(d):
    n = sqrt(d[0] ** 2 + d[1] ** 2)
    n_d = [d[0]/n, d[1] / n]
    return n_d


def initPosition():
    # Without corner
    on_sides = random.randint(0, 1)
    pos = [0, 0]
    screen = [SCREEN_WIDTH, SCREEN_HEIGHT]

    pos[on_sides] = random.randint(-SPAWN_SIZE, screen[on_sides] + SPAWN_SIZE)
    if pos[on_sides] > 0 and pos[on_sides] < screen[on_sides]:
        left = random.randint(0, 1)
        if left:
            pos[1-on_sides] = random.randint(-SPAWN_SIZE, 0)
        else:
            pos[1-on_sides] = random.randint(screen[1-on_sides],
                                             screen[1-on_sides] + SPAWN_SIZE)
    else:
        pos[1-on_sides] = random.randint(0, screen[1-on_sides])
    return pos


def initDirection(x, y):
    # Without corner
    on_sides = 0
    pos = [x, y]
    if x < 0 or x > SCREEN_WIDTH:
        on_sides = 1
        if (x > SCREEN_WIDTH):
            pos[0] = x - SCREEN_WIDTH
        else:
            pos[0] = -x
    if y > SCREEN_HEIGHT:
        pos[1] -= SCREEN_HEIGHT
    elif y < 0:
        pos[1] = -y

    screen = [SCREEN_WIDTH, SCREEN_HEIGHT]

    if pos[1-on_sides]:
        theta = atan(pos[on_sides] / pos[1-on_sides])/2
        theta_prime = atan(-(screen[on_sides] -
                             pos[on_sides]) / pos[1-on_sides])/2
    else:
        theta = atan(pi/2 * np.sign(pos[on_sides]))/2
        theta_prime = atan(-pi/2 * np.sign(screen[on_sides] -
                                           pos[on_sides])) / 2

    alpha = random.uniform(theta_prime, theta)

    if x < 0:
        return [cos(alpha), sin(alpha)]
    if y < 0:
        return [cos(pi/2 + alpha), sin(pi/2 + alpha)]
    if x > 0:
        return [cos(pi + alpha), sin(pi + alpha)]
    return [cos(3*pi/2 + alpha), sin(3*pi/2+alpha)]


class Missile():
    def __init__(self, h, w, s):
        self.x, self.y = initPosition()
        # self.x = x_pos  # float
        # self.y = y_pos  # float
        self.height = h  # float
        self.width = w  # float
        # 2 elements normés entre -1 et 1
        self.direction = initDirection(self.x, self.y)
        self.speed = s

    def move(self):
        self.x = self.speed * self.direction[0] + self.x
        self.y = self.speed * self.direction[1] + self.y

    def toDelete(self):
        # Return true or false
        if (self.x < - SPAWN_SIZE - MISSILE_HEIGHT or self.x > SCREEN_WIDTH + SPAWN_SIZE + MISSILE_HEIGHT) or (self.y < - SPAWN_SIZE - MISSILE_HEIGHT or self.y > SCREEN_HEIGHT + SPAWN_SIZE + MISSILE_HEIGHT):
            return True
        return False

    def hit(self):
        if x.square >= self.x.missile and x.square + SQUARE_WIDTH <= self.x.missile + MISSILE_WIDTH:
            if y.square >= self.y.missile and y.square + SQUARE_HEIGHT <= self.y.missile + MISSILE_HEIGHT:
                print("hit")
                return True
        return False
