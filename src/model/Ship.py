import numpy as np
import pygame
from model.Object import Object
from model.obstacle.attack.Soundwave import Soundwave


max_speed = np.array([300.0, 400.0])
min_speed = np.array([-max_speed[0], 200.0])
shooting_delay = 0.1
house = pygame.image.load("view/house.png")


class Ship(Object):

    def __init__(self, game):
        super().__init__(game)
        self.ship_width = 25
        self.ship_height = 35
        self.set_pos([375.0, 100.0])
        self.set_speed([0.0, min_speed[1]])
        self.acc = np.array([0,0])
        self.shooting = False
        self.shooting_counter = shooting_delay

    def get_hitbox(self):
        a = self.pos + [-self.ship_width/2, self.ship_height/2]
        b = self.pos + [self.ship_width/2, self.ship_height/2]
        c = self.pos + [self.ship_width/2, -self.ship_height/2]
        d = self.pos + [-self.ship_width/2, -self.ship_height/2]
        return np.array([a,b,c,d])

    def update_speed(self, dt):
        super().update_speed(dt)
        for i in range(len(self.speed)):
            if self.speed[i] > max_speed[i]:
                self.speed[i] = max_speed[i]
            if self.speed[i] < min_speed[i]:
                self.speed[i] = min_speed[i]

    def update_shooting(self, dt):
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

    def update_pos(self, dt):
        self.pos += dt * self.speed
        if self.pos[0] < 0 + self.ship_width//2:
            self.pos[0] = 0 + self.ship_width//2
            self.speed[0] = 0
        elif self.pos[0] > self.game.window_width - self.ship_width//2:
            self.pos[0] = self.game.window_width - self.ship_width//2
            self.speed[0] = 0

    def update(self, dt):
        super().update(dt)
        self.update_shooting(dt)

    def draw(self):
        scale = 3
        self.game.view.draw_image(self.pos[0], self.pos[1]+(35*(scale-1)), house, self.ship_width, self.ship_height, scale)
        # self.game.view.draw_rect(self.pos[0], self.pos[1], (255, 0, 0), self.ship_width, self.ship_width)