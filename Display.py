import pygame


class Display():
    def __init__(self, height, width):
        pygame.init()
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode((height, width))
        self.events = []
        self.pressed_down = False
        self.pressed_up = False
        self.pressed_left = False
        self.pressed_right = False

    def updateInput(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.pressed_up = True
                elif event.key == pygame.K_DOWN:
                    self.pressed_down = True
                elif event.key == pygame.K_LEFT:
                    self.pressed_left = True
                elif event.key == pygame.K_RIGHT:
                    self.pressed_right = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.pressed_up = False
                elif event.key == pygame.K_DOWN:
                    self.pressed_down = False
                elif event.key == pygame.K_LEFT:
                    self.pressed_left = False
                elif event.key == pygame.K_RIGHT:
                    self.pressed_right = False

    def getDirectionFromInput(self):
        direction = [0, 0]
        if (self.pressed_down):
            direction[1] = 1
        if (self.pressed_up):
            direction[1] = -1
        if (self.pressed_left):
            direction[0] = -1
        if (self.pressed_right):
            direction[0] = 1
        return direction

    def getEvents(self):
        self.events = self.pygame.event.get()

    def closingWindow(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                return True
        return False

    def drawSquare(self, square):
        self.pygame.draw.rect(self.screen, (0, 128, 255), pygame.Rect(square.x, square.y, square.height, square.width))

    def draw(self, square):
        self.screen.fill((0, 0, 0))
        self.drawSquare(square)
        self.pygame.display.flip()
