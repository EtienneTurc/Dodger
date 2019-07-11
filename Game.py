from Display import *
from Config import *


class Game():
    def __init__(self, square, missiles):
        self.square = square
        self.missiles = missiles
        self.display = Display(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.done = False

    def run(self):
        while not self.done:
            self.display.getEvents()
            self.done = self.display.closingWindow()
            self.display.updateInput()
            direction = self.display.getDirectionFromInput()
            self.square.updateDirection(direction)
            self.square.move()
            for missile in self.missiles:
                missile.move()
            self.display.draw(self.square, self.missiles)
