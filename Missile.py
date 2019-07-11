class Missile():
    def __init__(self, x_pos, y_pos, h, w, d, s):
        self.x = x_pos  # float
        self.y = y_pos  # float
        self.height = h  # float
        self.width = w  # float
        self.direction = d  # 2 elements normés entre -1 et 1
        self.speed = s

    def move(self):
        self.x = self.speed * self.direction[0] + self.x
        self.y = self.speed * self.direction[1] + self.y
