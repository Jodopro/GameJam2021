import numpy as np
import pygame
from model.Object import Object
from model.attack.Soundwave import Soundwave


max_speed = np.array([600.0, 500.0])
min_speed = np.array([-max_speed[0], 50.0])
shooting_delay = 0.1


class Ship(Object):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.set_pos([375.0, 100.0])
        self.set_speed([0.0, min_speed[1]])
        self.acc = np.array([0,0])
        self.shooting = False
        self.shooting_counter = 0

    def update(self, dt):
        self.speed += dt * self.acc
        for i in range(len(self.speed)):
            if self.speed[i] > max_speed[i]:
                self.speed[i] = max_speed[i]
            if self.speed[i] < min_speed[i]:
                self.speed[i] = min_speed[i]
        super().update(dt)

        self.shooting_counter += dt
        if self.shooting_counter >= shooting_delay:
            self.shooting_counter = shooting_delay
            if self.shooting:
                mouse_loc = pygame.mouse.get_pos()
                rel_x = mouse_loc[0]-self.pos[0]
                rel_y = self.game.view.transform_y(self.pos[1]) - mouse_loc[1]
                direction = np.array([rel_x, rel_y])
                new_wave = Soundwave(self.game, self.pos, self.speed, direction)
                self.game.add_object(new_wave)
                self.shooting_counter = 0

    def draw(self):
        self.game.view.draw_rect(self.pos[0], self.pos[1], (255, 0, 0), 25, 25)
