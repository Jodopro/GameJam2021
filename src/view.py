import pygame

PLAYER_OFFSET = 100
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 750


class View:
    def __init__(self, game, window):
        self.game = game
        self.window = window

    def transform_y(self, y):
        return WINDOW_HEIGHT - PLAYER_OFFSET - (y - self.game.ship.pos[1])

    def transform_x(self, x):
        return x

    def draw_circle(self, x, y, color, size):
        pygame.draw.circle(self.window, color, (self.transform_x(x), self.transform_y(y)), size)

    def draw_rect(self, x, y, color, width, height):
        pygame.draw.rect(self.window, color, (self.transform_x(x) - width//2, self.transform_y(y) - height//2, width, height))
