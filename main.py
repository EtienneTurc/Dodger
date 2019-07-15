from Square import *
from Game import *

square = Square(SQUARE_X, SQUARE_Y, SQUARE_HEIGHT,
                SQUARE_WDITH, [1, -1], SQUARE_SPEED)


game = Game(square)
game.run()
