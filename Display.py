import pygame
from math import *
from Config import *
from Utils import *
from readWrite import *


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
        self.pygame.draw.rect(self.screen, SQUARE_COLOR, pygame.Rect(
            square.x, square.y, square.height, square.width))

    def drawLives(self, lives):
            img = pygame.image.load('img/heart.png')
            img_resize = pygame.transform.scale(img, (20, 20))
            for i in range(lives):
                self.screen.blit(img_resize, (50 + i * 25, 25))

    def drawMissile(self, missile):
        image_orig = pygame.Surface((missile.height, missile.width))
        image_orig.set_colorkey((0, 0, 0))
        image_orig.fill(MISSILE_COLOR)
        image = image_orig.copy()
        image.set_colorkey((0, 0, 0))

        rect = image.get_rect()
        rect.center = (missile.x, missile.y)
        old_center = rect.center

        if missile.direction[0] == 0:
            rot = 180 + 90 * missile.direction[1]
        elif missile.direction[0] > 0:
            rot = atan(-missile.direction[1]/missile.direction[0]) * 180 / pi
        else:
            rot = atan(-missile.direction[1] /
                       missile.direction[0]) * 180 / pi + 180

        new_image = pygame.transform.rotate(image_orig, rot)
        rect = new_image.get_rect()
        rect.center = old_center
        self.screen.blit(new_image, rect)

    def drawScore(self, score):
        font = pygame.font.SysFont("comicsansms", 18)
        text = font.render("Score : " + str(score), True, (255, 255, 255))
        self.screen.blit(text, (SCREEN_WIDTH - 125, 25))

    def draw(self, square, missiles, score):
        self.screen.fill((0, 0, 0))
        self.drawSquare(square)
        for missile in missiles:
            self.drawMissile(missile)
        self.drawScore(score)
        self.drawDash(square.cd_dash)    
        self.drawLives(square.lives)
        self.pygame.display.flip()

    def retry(self):
        AAfilledRoundedRect(self.screen, pygame.Rect(
            BUTTON_X , BUTTON_Y , BUTTON_WIDTH + 3, BUTTON_HEIGHT + 3), BUTTON_COLOR_SHADOW, BUTTON_RADIUS)
        button = AAfilledRoundedRect(self.screen, pygame.Rect(
            BUTTON_X , BUTTON_Y , BUTTON_WIDTH, BUTTON_HEIGHT), BUTTON_COLOR, BUTTON_RADIUS)
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("RETRY", True, (255, 255, 255))
        self.screen.blit(text, (BUTTON_X ,BUTTON_Y))
        self.pygame.display.flip()
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    return True
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                return True
        return False

    def getDashEvent(self):
        for event in self.events:
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                return True
        return False

    def drawDash(self, cd_dash):
        if (cd_dash <= 0):
            cd_dash = 0
        img = pygame.image.load('img/Dash2.png')
        img_resize = pygame.transform.scale(img, (20, 20))
        self.screen.blit(img_resize, (25, 25))
        if cd_dash > 0:
            font = pygame.font.SysFont("comicsansms", 18)
            text = font.render(str(floor(cd_dash)), True, (255, 255, 255))
            self.screen.blit(text, (19, 22))

    def drawleaderboard(self,data):
        font = pygame.font.SysFont("comicsansms", 20)
        for i in range(len(data)):
            text = font.render(data[i][0] + '  :  ' + data[i][1], True, (255, 255, 255))
            self.screen.blit(text, (LEADERBOARD_X, LEADERBOARD_Y + i * 23))

