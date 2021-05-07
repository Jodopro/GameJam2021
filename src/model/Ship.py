import pygame
from model.Object import Object

dx_max = 600
dy_max = 500
dx_min = - dx_max
dy_min = 50

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
        if self.dy > dx_max:
            self.dy = dx_max
        elif self.dy < dy_min:
            self.dy = dy_min
        if self.dx > dx_max:
            self.dx = dx_max
        elif self.dx < dx_min:
            self.dx = dx_min
        self.y += dt * self.dy
        self.x += dt * self.dx

    def draw(self):
        self.game.view.draw_rect(self.x, self.y, (255, 0, 0), 25, 25)
