from Square import *
from Game import *
from Missile import *

square = Square(300, 300, 60, 60, [1, -1], 2)
missile = Missile(100, 50, 50, 10, [1, 1], 0.25)
missiles = [missile]

game = Game(square, missiles)
game.run()
