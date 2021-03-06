from model.obstacle.enemy.Enemy import Enemy
from model.obstacle.attack.Soundwave import Soundwave
import random
import numpy as np
from config import *


class Bird(Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        temp_y = int((1-BIRD_SPAWN_PLACE)*WINDOW_HEIGHT) + random.randrange(int(WINDOW_HEIGHT*BIRD_SPAWN_PLACE))
        y = game.ship.pos[1] - PLAYER_OFFSET + temp_y
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
        self.burst_counter = 0
        self.burst_wait_counter = 0

    def draw(self):
        # should never be used
        if self.speed[0] < 0:
            image = BALLOON_IMG
        else:
            image = BALLOON_IMG
        self.game.view.draw_image(self.pos[0], self.pos[1], image, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox(), self.color)

    def get_direction(self):
        rel_x = 1
        rel_y = 1
        return np.array([rel_x, rel_y])

    def update_shooting(self, dt):
        self.shooting_counter += dt
        if self.shooting_counter >= BIRD_SHOOTING_DELAY:
            direction = self.get_direction()
            self.shooting_counter = 0
            if self.burst_counter < BIRD_BURST:
                new_wave = Soundwave(self.game, origin=self.pos, speed=self.speed, direction=direction)
                self.game.add_object(new_wave)
                self.burst_counter += 1
            else:
                self.burst_wait_counter += 1
                if self.burst_wait_counter == BIRD_BURST_WAIT:
                    self.burst_counter = 0
                    self.burst_wait_counter = 0

    def update(self, dt):
        super().update(dt)
        self.update_shooting(dt)
