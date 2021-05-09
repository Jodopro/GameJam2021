from model.obstacle.enemy.Bird import Bird
import numpy as np
from config import *


class RandomBird(Bird):
    def get_direction(self):
        if self.speed[0] > 0:
            rel_x = random.random()
        else:
            rel_x = -random.random()
        rel_y = -random.random()
        return np.array([rel_x, rel_y])

    def draw(self):
        if self.speed[0] < 0:
            image = RANDOM_BIRD_IMG
        else:
            image = RANDOM_BIRD_FLIP_IMG
        self.game.view.draw_image(self.pos[0], self.pos[1], image, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox(), self.color)