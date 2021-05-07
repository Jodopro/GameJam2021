import pygame, sys, time, math, random
from pygame.locals import *
from model.Game import Game

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)

basicFont = pygame.font.SysFont(None, 48)

window = pygame.display.set_mode((750, 1000), 0, 32)

pygame.display.update()

homeLoc = [250, 500]
homeSpeed = [0, 0]
lastTime = time.time()


game = Game(window)
game.update(0)
game.draw()
pygame.display.update()
while True:
    currentTime = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                game.ship.ddy += 100
            elif event.key == K_a:
                game.ship.ddx -= 100
            elif event.key == K_s:
                game.ship.ddy -= 100
            elif event.key == K_d:
                game.ship.ddx += 100
        elif event.type == KEYUP:
            if event.key == K_w:
                game.ship.ddy -= 100
            elif event.key == K_a:
                game.ship.ddx += 100
            elif event.key == K_s:
                game.ship.ddy += 100
            elif event.key == K_d:
                game.ship.ddx -= 100
    game.update(currentTime-lastTime)
    game.draw()
    pygame.display.update()
    lastTime = currentTime
