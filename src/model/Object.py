import numpy as np
import pygame


class Object:
    pos = np.array([0.0,0.0])
    speed = np.array([0.0,0.0])
    acc = np.array([0.0,0.0])

    tiny_star = pygame.image.load("view/tiny_star.png")
    small_star = pygame.image.load("view/small_star.png")
    medium_star = pygame.image.load("view/medium_star.png")
    large_star = pygame.image.load("view/large_star.png")
    big_star = pygame.image.load("view/big_star.png")

    stars = [tiny_star, small_star, medium_star, large_star, big_star]


    def __init__(self,game):
        self.game = game

    def set_pos(self, new_position):
        self.pos = np.array(new_position)

    def set_speed(self, new_speed):
        self.speed = np.array(new_speed)

    def set_acc(self, new_acc):
        self.acc = np.array(new_acc)

    def draw(self):
        pass

    def update_speed(self, dt):
        self.speed += dt * self.acc

    def update_pos(self, dt):
        self.pos += dt * self.speed

    def update(self, dt):
        self.update_speed(dt)
        self.update_pos(dt)
