from model.obstacle.enemy.Enemy import Enemy
from model.obstacle.attack.Soundwave import Soundwave
import random, pygame
from view import PLAYER_OFFSET
import numpy as np
import pygame


shooting_delay = 0.1
space_bird = pygame.image.load("view/spaceship.png")


class Bird(Enemy):
    def __init__(self, game):
        super().__init__(game)
        self.game = game
        y = game.ship.pos[1] + game.window_height//2 - PLAYER_OFFSET + random.randrange(game.window_height//2)
        v_speed = random.randrange(50, 100)
        if random.random() > 0.5:
            x = 0
            self.speed = np.array([250.0, v_speed])
        else:
            x = game.window_width
            self.speed = np.array([-250.0, v_speed])
        self.aim_offset = random.randrange(-200, 200)
        self.pos = np.array([x, y])
        self.shooting_counter = 0
        self.width = 100
        self.height = 50

    def draw(self):
        self.game.view.draw_image(self.pos[0], self.pos[1], space_bird, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox())
        # self.game.view.draw_circle(self.pos[0], self.pos[1], (0, 0, 255), 15)

    def update_shooting(self, dt):
        self.shooting_counter += dt
        if self.shooting_counter >= shooting_delay:
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
