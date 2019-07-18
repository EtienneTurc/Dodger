from Display import *
from Config import *
from Missile import *
import time


class Game():
    def __init__(self, square):
        self.square = square
        self.missiles = []
        self.display = Display(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.done = False
        self.time_between_missiles = TIME_BETWEEN_MISSILES
        self.time_last_missile = 0
        self.score = 0

    def run(self):
        while not self.done:
            current_time = int(round(time.time() * 1000))
            self.display.getEvents()
            self.done = self.display.closingWindow()
            self.display.updateInput()
            direction = self.display.getDirectionFromInput()

            self.square.updateDirection(direction)
            self.square.move()

            if (current_time - self.time_last_missile >= self.time_between_missiles):
                self.missiles.append(
                    Missile(MISSILE_HEIGHT, MISSILE_WIDTH, MISSILE_SPEED))
                self.time_last_missile = current_time
            for missile in self.missiles:
                missile.move()
                if (missile.toDelete()):
                    self.missiles.remove(missile)
                if (missile.hit(self.square)):
                    self.missiles.remove(missile)

            self.display.draw(self.square, self.missiles)
