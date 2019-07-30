from Display import *
from Config import *
from Missile import *
from Square import *
import time
import readWrite


class Game():
    def __init__(self):
        self.square = Square(SQUARE_X, SQUARE_Y, SQUARE_HEIGHT,
                             SQUARE_WIDTH, [0, 0], SQUARE_SPEED)
        self.missiles = []
        self.display = Display(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.done_game = True
        self.done_all = False
        self.time_between_missiles = TIME_BETWEEN_MISSILES
        self.time_last_missile = 0
        self.score = 0

    def run(self):
        while not self.done_all:
            self.display.getEvents()
            self.done_all = self.display.closingWindow()
            leaderboard = readWrite.readCsv()
            self.display.drawleaderboard(leaderboard)
            if self.display.retry():
                self.__init__()
                self.done_game = False

            current_time = int(round(time.time() * 1000))
            while not self.done_game:
                last_time = current_time
                current_time = int(round(time.time() * 1000))
                self.display.getEvents()
                self.done_game = self.display.closingWindow()
                self.done_all = self.done_game
                self.display.updateInput()

                direction = self.display.getDirectionFromInput()
                self.square.updateDirection(direction)
                self.square.move((current_time - last_time)/1000)
                if self.display.getDashEvent():
                    self.square.dash()

                if (current_time - self.time_last_missile >= self.time_between_missiles):
                    self.missiles.append(
                        Missile(MISSILE_HEIGHT, MISSILE_WIDTH, MISSILE_SPEED))
                    self.time_between_missiles -= 0.5
                    self.score += 1
                    self.time_last_missile = current_time
                for missile in self.missiles:
                    missile.move((current_time - last_time)/1000)
                    if (missile.toDelete()):
                        self.missiles.remove(missile)
                    if (missile.hit(self.square)):
                        self.square.decreaseLife()
                        self.missiles.remove(missile)
                    if self.square.lives <= 0:
                        self.done_game = True
                        readWrite.writeInCsv(self.score)
                        
                self.display.draw(self.square, self.missiles, self.score)
