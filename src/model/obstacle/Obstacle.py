from model.Object import Object
import numpy as np


class Obstacle(Object):

    def __init__(self, game, color=(255,255, 255), width=100, height=100):
        super().__init__(game)
        self.color = color
        self.width = width
        self.height = height

    def get_hitbox(self):
        a = self.pos + [-self.width / 2, self.height / 2]
        b = self.pos + [self.width / 2, self.height / 2]
        c = self.pos + [self.width / 2, -self.height / 2]
        d = self.pos + [-self.width / 2, -self.height / 2]
        return np.array([a, b, c, d])


    def draw(self):
        self.game.view.draw_rect(self.pos[0], self.pos[1], self.color, self.width, self.height)
