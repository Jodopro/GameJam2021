from model.obstacle.enemy.Enemy import Enemy
from model.obstacle.attack.Soundwave import Soundwave
import random
import numpy as np
from config import *


class Bird(Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        y = game.ship.pos[1] + WINDOW_HEIGHT//2 - PLAYER_OFFSET + random.randrange(WINDOW_HEIGHT//2)
        v_speed = random.randrange(50, 100)
        if random.random() > 0.5:
            x = 0
            self.speed = np.array([250.0, v_speed])
        else:
            x = WINDOW_WIDTH
            self.speed = np.array([-250.0, v_speed])
        self.aim_offset = random.randrange(-200, 200)
        self.pos = np.array([x, y])
        self.shooting_counter = 0
        self.width = 100
        self.height = 50

    def draw(self):
        self.game.view.draw_image(self.pos[0], self.pos[1], BIRD_IMG, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox())

    def update_shooting(self, dt):
        self.shooting_counter += dt
        if self.shooting_counter >= BIRD_SHOOTING_DELAY:
            rel_x = self.game.ship.pos[0]-self.pos[0]
            rel_y = self.game.ship.pos[1]-self.pos[1]+self.aim_offset
            if (rel_x > 0 and self.speed[0] > 0) or (rel_x < 0 and self.speed[0] < 0):
                direction = np.array([rel_x, rel_y])
                new_wave = Soundwave(self.game, self.pos, self.speed, direction)
                self.game.add_object(new_wave)
                self.shooting_counter = 0

    def update(self, dt):
        super().update(dt)
        self.update_shooting(dt)
