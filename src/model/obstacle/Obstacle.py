from model.Object import Object
import numpy as np
import util
import enum


class Obstacle(Object):
    # todo matteo: refactor all models such that they make use of kwargs and args where possible
    class Nature(enum.Enum):
        Hostile = 1
        Neutral = 2
        Friendly = 3

    def __init__(self, game, color=(0, 255, 0), width=100, height=100, direction=[0.0, 1.0],
                 nature=Nature.Neutral):
        super().__init__(game)
        self.color = color
        self.width = width
        self.height = height
        self.direction = direction / np.linalg.norm(direction)
        self.nature = nature

    def get_hitbox(self):
        a = self.pos + util.rotate_in_direction([-self.width / 2, self.height / 2], self.direction)
        b = self.pos + util.rotate_in_direction([self.width / 2, self.height / 2], self.direction)
        c = self.pos + util.rotate_in_direction([self.width / 2, -self.height / 2], self.direction)
        d = self.pos + util.rotate_in_direction([-self.width / 2, -self.height / 2], self.direction)
        box = np.array([a, b, c, d])
        return box

    def draw(self):
        self.game.view.draw_rect(self.pos[0], self.pos[1], self.color, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox(), self.color)
