import pygame
import numpy as np

from model.obstacle.attack.Attack import Attack

wave_speed = 500
width_expansion = 50
wave = pygame.image.load("view/soundwave.png")

class Soundwave(Attack):
    def __init__(self, game, origin, speed, direction):
        super().__init__(game)
        self.game = game
        self.pos = origin.copy()
        self.speed = speed.copy()
        self.direction = direction/np.linalg.norm(direction)
        self.speed += self.direction*wave_speed
        self.width = 10
        self.height = 10
        self.color = (0, 255, 0)

    def draw(self):
        self.game.view.draw_hitbox(self.get_hitbox())
        self.game.view.draw_rect(self.pos[0], self.pos[1], self.color, self.width, self.height, self.direction)
        # self.game.view.draw_wave(self.pos[0], self.pos[1], wave, self.width, 10, self.direction)

    def update(self, dt):
        super().update(dt)
        self.width += dt * width_expansion
