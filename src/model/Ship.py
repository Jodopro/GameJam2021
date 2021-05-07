import pygame
from src.model.Object import Object


class Ship(Object):
    player_y = 100
    player_x = 375
    player_dx = 0
    player_dy = 25
    player_ddx = 0
    player_ddy = 0

    def __init__(self, game):
        self.game = game

    def update(self, dt):
        self.player_dx += dt*self.player_ddx
        self.player_dy += dt*self.player_ddy
        if self.player_dy > 500:
            self.player_dy = 500
        elif self.player_dy < 50:
            self.player_dy = 50
        if self.player_dx > 50:
            self.player_dx = 50
        elif self.player_dx < -50:
            self.player_dx = -50
        self.player_y += dt * self.player_dy
        self.player_x += dt * self.player_dx

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.player_x, self.game.WINDOW_HEIGHT - 100, 25, 25))