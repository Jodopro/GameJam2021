from model.obstacle.enemy.Enemy import Enemy
from model.attack.Soundwave import Soundwave
import random
from src.view import PLAYER_OFFSET
import numpy as np


shooting_delay = 0.1


class Bird(Enemy):
    def __init__(self, game):
        self.game = game
        y = game.ship.pos[1] + game.window_height//2 - PLAYER_OFFSET + random.randrange(game.window_height//2)
        if random.random() > 0.5:
            x = 0
            self.speed = np.array([250.0, 80.0])
        else:
            x = game.window_width
            self.speed = np.array([-250.0, 80.0])
        self.pos = np.array([x, y])
        self.shooting_counter = 0

    def draw(self):
        self.game.view.draw_circle(self.pos[0], self.pos[1], (0, 0, 255), 15)

    def update_shooting(self, dt):
        self.shooting_counter += dt
        if self.shooting_counter >= shooting_delay:
            rel_x = self.game.ship.pos[0]-self.pos[0]
            rel_y = self.game.ship.pos[1]-self.pos[1]
            if (rel_x > 0 and self.speed[0] > 0) or (rel_x < 0 and self.speed[0] < 0):
                direction = np.array([rel_x, rel_y])
                new_wave = Soundwave(self.game, self.pos, self.speed, direction)
                self.game.add_object(new_wave)
                self.shooting_counter = 0

    def update(self, dt):
        super().update(dt)
        self.update_shooting(dt)
