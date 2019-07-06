from cube import *
import pygame

mycube = cube(300, 300, 60, 60, [1, -1], 2)

# voila

pygame.init()
screen = pygame.display.set_mode((1200, 1000))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            mycube.move()
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(
        mycube.x, mycube.y, mycube.height, mycube.width))
    pygame.display.flip()
