def checkDirection(direction):
    if len(direction) != 2 and (direction[0] > 1 or direction[0] < -1) and (direction[1] > 1 or direction[1] < -1):
        return [0, 0]
    else:
        return direction

def canMove(x_virtual, y_virtual, height, width):
    if (x_virtual < 0 or x_virtual > 1500- height) or (y_virtual < 0 or y_virtual > 800 - width): 
        return False
    return True


class Square():
    def __init__(self, x_pos, y_pos, h, w, d, s):
        self.x = x_pos  # float
        self.y = y_pos  # float
        self.height = h  # float
        self.width = w  # float
        self.direction = d  # 2 elements => valeurs possibles -1 0 ou 1
        self.speed = s  # float

    def move(self):
        x_virtual = self.speed * self.direction[0] + self.x
        y_virtual = self.speed * self.direction[1] + self.y
        height = self.height
        width = self.width
        print(x_virtual)
        if canMove(x_virtual, y_virtual, height, width):
            self.x = self.speed * self.direction[0] + self.x
            self.y = self.speed * self.direction[1] + self.y

    def updateDirection(self, direction):
        self.direction = direction

    # def checkPosition(self):
    #     if (x < 0 or x > 1200 - height) and (y < 0 or y > 1000 - widht):
    #         return 
    #     else:
    #         return x, y

# mycube = player(x, y)
# mycube.move()
