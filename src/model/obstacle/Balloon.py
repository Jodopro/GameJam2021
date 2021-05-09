from model.obstacle.Obstacle import Obstacle

from config import *


class Balloon(Obstacle): 
    def __init__(self, game, ship):
        super().__init__(game, width=50, height=75)
        self.ship = ship

    def update_speed(self, dt):
        self.speed = self.ship.speed.copy()

    def update_pos(self, dt):
        self.pos = self.ship.pos.copy()
        self.pos[1] += 75

    def draw(self):
        self.game.view.draw_image(self.pos[0], self.pos[1], BALLOON_IMG, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox())
