import sys
import time
from pygame.locals import *
from model.Game import Game
from config import *

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

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)


def start_screen():
    window.fill((0, 0, 0))
    line1 = basicFont.render("Bananas are Berries", False, (255, 255, 255))
    window.blit(line1, (30, 10))
    line2 = basicFont.render("Press any key to start", False, (255, 255, 255))
    window.blit(line2, (30, 100))
    pygame.display.update()
    exit_start_screen = False
    while not exit_start_screen:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYUP:
                exit_start_screen = True
    while True:
        current_pressed = pygame.key.get_pressed()
        run_game(current_pressed)


def end_screen(score):
    window.fill((0, 0, 0))
    line1 = basicFont.render("Bananas are Berries", False, (255, 255, 255))
    window.blit(line1, (30, 10))
    line2 = basicFont.render("Score was: "+str(score), False, (255, 255, 255))
    window.blit(line2, (30, 110))
    line3 = basicFont.render("Press any key to try again", False, (255, 255, 255))
    window.blit(line3, (30, 210))
    pygame.display.update()
    exit_end_screen = False
    new_pressed = []
    while not exit_end_screen:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                new_pressed.append(event.key)
            elif event.type == KEYUP:
                if event.key in new_pressed:
                    exit_end_screen = True


def run_game(current_pressed):
    lastTime = time.time()
    game = Game(window)
    game.update(0)
    game.draw()
    if current_pressed[K_w]:
        game.ship.acc[1] += 1000
    if current_pressed[K_a]:
        game.ship.acc[0] -= 1000
    if current_pressed[K_s]:
        game.ship.acc[1] -= 1000
    if current_pressed[K_d]:
        game.ship.acc[0] += 1000
    if current_pressed[K_SPACE]:
        game.ship.shooting = True
    pygame.display.update()
    while True:
        currentTime = time.time()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_w:
                    game.ship.acc[1] += 1000
                elif event.key == K_a:
                    game.ship.acc[0] -= 1000
                elif event.key == K_s:
                    game.ship.acc[1] -= 1000
                elif event.key == K_d:
                    game.ship.acc[0] += 1000
                elif event.key == K_SPACE:
                    game.ship.wants_to_shoot = True
            elif event.type == KEYUP:
                if event.key == K_w:
                    game.ship.acc[1] -= 1000
                elif event.key == K_a:
                    game.ship.acc[0] += 1000
                elif event.key == K_s:
                    game.ship.acc[1] += 1000
                elif event.key == K_d:
                    game.ship.acc[0] -= 1000
                elif event.key == K_SPACE:
                    game.ship.stop_shooting()
        dt = currentTime - lastTime
        if PRINT_TIME:
            print(dt)
        game.update(dt)
        game.draw()
        pygame.display.update()
        lastTime = currentTime
        if game.finished:
            break
    end_screen(game.score)




if __name__ == '__main__':
    start_screen()