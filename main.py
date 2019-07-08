from Cube import *
from Game import *

cube = Cube(300, 300, 60, 60, [1, -1], 2)

game = Game(cube)
game.run()
