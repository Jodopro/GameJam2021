import numpy as np
import pygame
from model.Object import Object


max_speed = np.array([600.0, 500.0])
min_speed = np.array([-max_speed[0], 50.0])


class Ship(Object):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.set_pos([375.0, 100.0])
        self.set_speed([0.0, min_speed[1]])
        self.acc = np.array([0,0])

    def set_acc(self, new_acc):
        self.acc = np.array(new_acc)


    def update(self, dt):
        self.speed += dt * self.acc
        for i in range(len(self.speed)):
            if self.speed[i] > max_speed[i]:
                self.speed[i] = max_speed[i]
            if self.speed[i] < min_speed[i]:
                self.speed[i] = min_speed[i]
        self.pos += dt * self.speed

    def draw(self):
        self.game.view.draw_rect(self.pos[0], self.pos[1], (255, 0, 0), 25, 25)
