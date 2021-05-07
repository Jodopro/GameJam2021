import pygame, sys, time, math, random
from pygame.locals import *

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

window = pygame.display.set_mode((500, 500), 0, 32)

pygame.display.update()

homeLoc = [250, 500]
homeSpeed = [0, 0]
lastTime = time.time()


def update_home(dt):
    pygame.draw.rect(window, BLACK, (homeLoc[0], homeLoc[1], 25, 25))
    dx = dt*homeSpeed[0]
    dy = dt*homeSpeed[1]
    homeLoc[0] += dx
    homeLoc[1] += dy
    pygame.draw.rect(window, WHITE, (homeLoc[0], homeLoc[1], 25, 25))


pygame.display.update()
while True:
    currentTime = time.time()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_w:
                homeSpeed[1] -= 5
            elif event.key == K_a:
                homeSpeed[0] -= 5
            elif event.key == K_s:
                homeSpeed[1] += 5
            elif event.key == K_d:
                homeSpeed[0] += 5
    update_home(currentTime-lastTime)
    pygame.display.update()
    lastTime = currentTime
