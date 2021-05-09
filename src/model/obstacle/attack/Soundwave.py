import pygame
import numpy as np

from model.obstacle.Obstacle import Obstacle
from model.obstacle.attack.Attack import Attack

from config import *


class Soundwave(Attack):

    def __init__(self, *args, direction, color=(0, 255, 0), width=10, height=10,
                 **kwargs):
        super().__init__(*args, color=color, width=width, height=height, direction=direction, **kwargs)
        self.speed += self.direction * WAVE_SPEED
        # todo: remove the is_enemy, replace it by self.nature

    def draw(self):
        self.game.view.draw_hitbox(self.get_hitbox(), self.color)
        if self.nature == Obstacle.Nature.Hostile:
            self.game.view.draw_image(self.pos[0], self.pos[1], WAVE_ENEMY_PNG, self.width, 10, self.direction)
        else:
            wave = WAVE_RAINBOW_PNG
            if (HOUSE_IMG == POLICE_BOX_SHINY):
                wave = WAVE_ARRAY[int(10*random.random())]
            self.game.view.draw_image(self.pos[0], self.pos[1], wave, self.width, 10, self.direction)

    def update(self, dt):
        super().update(dt)
        self.width += dt * WAVE_WIDTH_EXPANSION
