from Display import *


class Game():
    def __init__(self, square):
        self.square = square
        self.display = Display(1500, 800)
        self.done = False

    def run(self):
        while not self.done:
            self.display.getEvents()
            self.done = self.display.closingWindow()
            self.display.updateInput()
            direction = self.display.getDirectionFromInput()
            self.square.updateDirection(direction)
            self.square.move()
            self.display.draw(self.square)
