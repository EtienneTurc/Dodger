from math import *
import random
from Config import *
import numpy as np


def norm(d):
    n = sqrt(d[0] ** 2 + d[1] ** 2)
    n_d = [d[0]/n, d[1] / n]
    return n_d


# def intersect(A, B, directionA, directionB):
#     # Peut être pas ouf
#     if directionA[0] == 0 and directionB == 0:
#         return False

#     elif directionA[0] == 0:
#         slope_b = directionB[1] / directionB[0]
#         ord_b = B[1] - slope_b * B[0]
#         return [A[0], slope_b*A[0] + ord_b]

#     elif directionB[0] == 0:
#         slope_a = directionA[1] / directionA[0]
#         ord_a = A[1] - slope_a * A[0]
#         return [B[0], slope_a*B[0] + ord_a]

#     slope_a = directionA[1] / directionA[0]
#     slope_b = directionB[1] / directionB[0]
#     ord_a = A[1] - slope_a * A[0]
#     ord_b = B[1] - slope_b * B[0]
#     den = slope_a - slope_b
#     if A[0] * B[1] == B[0] * A[1]:
#         x = (ord_b - ord_a)/den
#         y = (slope_a * ord_b - slope_b * ord_a)/den
#         return x, y
#     return False


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
    if x > SCREEN_WIDTH:
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
        if (self.x < - SPAWN_SIZE - self.height or self.x > SCREEN_WIDTH + SPAWN_SIZE + self.height) or (self.y < - SPAWN_SIZE - self.height or self.y > SCREEN_HEIGHT + SPAWN_SIZE + self.height):
            return True
        return False

    def hit(self, square):
        # rotation from center
        demi_diag = sqrt(self.height**2 + self.width**2) / 2
        left_top = [self.x - demi_diag * self.direction[0],
                    self.y - demi_diag * self.direction[1]]
        right_top = [self.x + demi_diag * self.direction[0],
                     self.y - demi_diag * self.direction[1]]
        left_bot = [self.x - demi_diag * self.direction[0],
                    self.y + demi_diag * self.direction[1]]
        right_bot = [self.x + demi_diag * self.direction[0],
                     self.y + demi_diag * self.direction[1]]
        # rotation top left
        # diag = sqrt(self.height**2 + self.width**2)
        # left_top = [self.x, self.y]
        # right_top = [self.x + self.width * self.direction[0],
        #              self.y + self.width * self.direction[1]]
        # left_bot = [self.x + self.height * self.direction[0],
        #             self.y + self.height * self.direction[1]]
        # right_bot = [self.x + diag * self.direction[0],
        #              self.y + diag * self.direction[1]]

        summits = [left_top, right_top, left_bot, right_bot]

        for s in summits:
            if square.x <= s[0] and square.x + square.width >= s[0] and square.y <= s[1] and square.y + square.height >= s[1]:
                return True
        return False
