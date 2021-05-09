import pygame
import numpy as np

from model.obstacle.attack.Attack import Attack

from config import *

class Soundwave(Attack):
    def __init__(self, game, origin, speed, direction, is_enemy=False):
        super().__init__(game)
        self.game = game
        self.pos = origin.copy()
        self.speed = speed.copy()
        self.direction = direction/np.linalg.norm(direction)
        self.speed += self.direction*WAVE_SPEED
        self.width = 10
        self.height = 10
        self.color = (0, 255, 0)
        self.is_enemy = is_enemy

    def draw(self):
        self.game.view.draw_hitbox(self.get_hitbox())
        if self.is_enemy:
            self.game.view.draw_image(self.pos[0], self.pos[1], WAVE_ENEMY_PNG, self.width, 10, self.direction)
        else:
            self.game.view.draw_image(self.pos[0], self.pos[1], WAVE_RAINBOW_PNG, self.width, 10, self.direction)

    def update(self, dt):
        super().update(dt)
        self.width += dt * WAVE_WIDTH_EXPANSION
