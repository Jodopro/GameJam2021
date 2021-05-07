import pygame
from model.Object import Object


class Ship(Object):
    y = 100
    x = 375
    dx = 0
    dy = 25
    ddx = 0
    ddy = 0

    def __init__(self, game):
        self.game = game

    def update(self, dt):
        self.dx += dt*self.ddx
        self.dy += dt*self.ddy
        if self.dy > 500:
            self.dy = 500
        elif self.dy < 50:
            self.dy = 50
        if self.dx > 50:
            self.dx = 50
        elif self.dx < -50:
            self.dx = -50
        self.y += dt * self.dy
        self.x += dt * self.dx

    def draw(self):
        self.game.view.draw_rect(self.x, self.y, (255, 0, 0), 25, 25)
