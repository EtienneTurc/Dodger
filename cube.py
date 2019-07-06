def checkDirection(direction):
    if len(direction) != 2 and (direction[0] > 1 or direction[0] < -1) and (direction[1] > 1 or direction[1] < -1):
        return [0, 0]
    else:
        return direction


class cube():
    def __init__(self, x_pos, y_pos, h, w, d, s):
        self.x = x_pos  # float
        self.y = y_pos  # float
        self.height = h  # float
        self.width = w  # float
        self.direction = d  # 2 elements => valeurs possibles -1 0 ou 1
        self.speed = s  # float

    def move(self):
        self.x = self.speed * self.direction[0] + self.x
        self.y = self.speed * self.direction[1] + self.y
        print(self.x)
        print(self.y)

    def updateDirection(self, direction):
        self.direction = direction


# mycube = player(x, y)
# mycube.move()
