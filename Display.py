import pygame
from math import *


class Display():
    def __init__(self, height, width):
        pygame.init()
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode((height, width))
        self.events = []
        self.pressed_down = False
        self.pressed_up = False
        self.pressed_left = False
        self.pressed_right = False

    def updateInput(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pressed_up = True
                elif event.key == pygame.K_DOWN:
                    self.pressed_down = True
                elif event.key == pygame.K_LEFT:
                    self.pressed_left = True
                elif event.key == pygame.K_RIGHT:
                    self.pressed_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.pressed_up = False
                elif event.key == pygame.K_DOWN:
                    self.pressed_down = False
                elif event.key == pygame.K_LEFT:
                    self.pressed_left = False
                elif event.key == pygame.K_RIGHT:
                    self.pressed_right = False

    def getDirectionFromInput(self):
        direction = [0, 0]
        if (self.pressed_down):
            direction[1] = 1
        if (self.pressed_up):
            direction[1] = -1
        if (self.pressed_left):
            direction[0] = -1
        if (self.pressed_right):
            direction[0] = 1
        return direction

    def getEvents(self):
        self.events = self.pygame.event.get()

    def closingWindow(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return True
        return False

    def drawSquare(self, square):
        self.pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(
            square.x, square.y, square.height, square.width))

    def drawMissile(self, missile):
        image_orig = pygame.Surface((missile.height, missile.width))
        image_orig.set_colorkey((0, 0, 0))
        image_orig.fill((255, 0, 0))
        image = image_orig.copy()
        image.set_colorkey((0, 0, 0))

        rect = image.get_rect()
        rect.center = (missile.x, missile.y)
        old_center = rect.center

        if missile.direction[0] == 0:
            rot = 180 + 90 * missile.direction[1]
        elif missile.direction[0] > 0:
            rot = atan(-missile.direction[1]/missile.direction[0]) * 180 / pi
        else:
            rot = atan(-missile.direction[1] /
                       missile.direction[0]) * 180 / pi + 180

        new_image = pygame.transform.rotate(image_orig, rot)
        rect = new_image.get_rect()
        rect.center = old_center
        self.screen.blit(new_image, rect)

    def draw(self, square, missiles):
        self.screen.fill((0, 0, 0))
        self.drawSquare(square)
        for missile in missiles:
            self.drawMissile(missile)
        self.pygame.display.flip()


# tan(O) = oppposé / adjacent = y / x
# O = arctan(y/x)
# [x_rad, 2PI] radian
# [x_degré, 360] degré


# ------------
#  -
#   -
#    -
#     -
#      -
#       -
#        -

#            |
# ------------|
#           -
#          -
#         -
#        -
#       -
#      -
#     -
