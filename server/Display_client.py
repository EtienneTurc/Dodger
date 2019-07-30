import pygame
from math import *
from Config import *
from Utils import *


class Display():
    def __init__(self, height, width):
        pygame.init()
        self.pygame = pygame
        self.screen = self.pygame.display.set_mode((height, width))

    def drawSquare(self, square):
        self.pygame.draw.rect(self.screen, SQUARE_COLOR, pygame.Rect(
            square[0], square[1], square[2], square[3]))

    def drawLives(self, lives):
        img = pygame.image.load('img/heart.png')
        img_resize = pygame.transform.scale(img, (20, 20))
        for i in range(lives):
            self.screen.blit(img_resize, (50 + i * 25, 25))

    def drawMissile(self, missile):
        image_orig = pygame.Surface((missile[2], missile[3]))
        image_orig.set_colorkey((0, 0, 0))
        image_orig.fill(MISSILE_COLOR)
        image = image_orig.copy()
        image.set_colorkey((0, 0, 0))

        rect = image.get_rect()
        rect.center = (missile[0], missile[1])
        old_center = rect.center

        if missile[4] == 0:
            rot = 180 + 90 * missile[5]
        elif missile[4] > 0:
            rot = atan(-missile[5]/missile[4]) * 180 / pi
        else:
            rot = atan(-missile[5] /
                       missile[4]) * 180 / pi + 180

        new_image = pygame.transform.rotate(image_orig, rot)
        rect = new_image.get_rect()
        rect.center = old_center
        self.screen.blit(new_image, rect)

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
            SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2-5, BUTTON_WIDTH + 3, BUTTON_HEIGHT + 3), BUTTON_COLOR_SHADOW, BUTTON_RADIUS)
        button = AAfilledRoundedRect(self.screen, pygame.Rect(
            SCREEN_WIDTH / 2 - 20, SCREEN_HEIGHT / 2-5, BUTTON_WIDTH, BUTTON_HEIGHT), BUTTON_COLOR, BUTTON_RADIUS)
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render("RETRY", True, (255, 255, 255))
        self.screen.blit(text, (SCREEN_WIDTH / 2 - 5, SCREEN_HEIGHT / 2 + 5))
        self.pygame.display.flip()
        for event in self.events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if button.collidepoint(pos):
                    return True
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                return True
        return False
