from model.Object import Object
import numpy as np
import util


class Obstacle(Object):

    def __init__(self, game, color=(255,255, 255), width=100, height=100, direction=[0.0,0.1]):
        super().__init__(game)
        self.color = color
        self.width = width
        self.height = height
        self.direction = direction

    def get_hitbox(self):
        a = self.pos + util.rotate_in_direction([-self.width / 2, self.height / 2], self.direction)
        b = self.pos + util.rotate_in_direction([self.width / 2, self.height / 2], self.direction)
        c = self.pos + util.rotate_in_direction([self.width / 2, -self.height / 2], self.direction)
        d = self.pos + util.rotate_in_direction([-self.width / 2, -self.height / 2], self.direction)
        box = np.array([a,b,c,d])
        return box


    def draw(self):
        self.game.view.draw_rect(self.pos[0], self.pos[1], self.color, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox())
