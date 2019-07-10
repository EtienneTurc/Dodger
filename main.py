from Square import *
from Game import *

square = Square(300, 300, 60, 60, [1, -1], 2)

game = Game(square)
game.run()
