from Square import *
from Game import *
from Missile import *

square = Square(300, 300, 60, 60, [1, -1], 1)
missiles = [Missile(20, 3, [1, 1], 0.25) for i in range(4)]

game = Game(square, missiles)
game.run()
