from model.obstacle.enemy.Bird import Bird
import numpy as np
from config import *


class AimedBird(Bird):
    def get_direction(self):
        rel_x = self.game.ship.pos[0] - self.pos[0]
        rel_y = self.game.ship.pos[1] - self.pos[1] + self.aim_offset
        return np.array([rel_x, rel_y])

    def draw(self):
        if self.speed[0] < 0:
            image = AIMED_BIRD_IMG
        else:
            image = AIMED_BIRD_FLIP_IMG
        self.game.view.draw_image(self.pos[0], self.pos[1], image, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox(), self.color)