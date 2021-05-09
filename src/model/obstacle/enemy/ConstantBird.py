from model.obstacle.enemy.Bird import Bird
import numpy as np
import random
from config import *


class ConstantBird(Bird):
    def __init__(self, game):
        super().__init__(game)
        if self.speed[0]>0:
            rel_x = random.random()
        else:
            rel_x = -random.random()
        rel_y = -random.random()
        self.attack_angle = np.array([rel_x, rel_y])

    def get_direction(self):
        return self.attack_angle

    def draw(self):
        if self.speed[0] < 0:
            image = CONSTANT_BIRD_IMG
        else:
            image = CONSTANT_BIRD_FLIP_IMG
        self.game.view.draw_image(self.pos[0], self.pos[1], image, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox(), self.color)