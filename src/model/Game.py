import random, pygame
from model.Ship import Ship
from view import View


class Game:
    stars = []
    ship = None
    HEIGHT = 10000
    WIDTH = 750

    def __init__(self, window):
        self.view = View(self, window)
        self.ship = Ship(self)
        for i in range(1000):
            x = random.randrange(self.WIDTH)
            y = random.randrange(self.HEIGHT)
            size = random.randrange(2, 6)
            self.stars.append((x, y, size))

    def update(self, dt):
        self.ship.update(dt)

    def draw(self):
        self.view.window.fill((0, 0, 0))
        for (x, y, size) in self.stars:
            self.view.draw_circle(x, y, (255, 255, 255), size)
        self.ship.draw()
