from Display import *


class Game():
    def __init__(self, cube):
        self.cube = cube
        self.display = Display(1200, 1000)
        self.done = False

    def run(self):
        while not self.done:
            self.display.getEvents()
            self.done = self.display.closingWindow()
            self.display.updateInput()
            direction = self.display.getDirectionFromInput()
            self.cube.updateDirection(direction)
            self.cube.move()
            self.display.draw(self.cube)
