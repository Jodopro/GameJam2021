import random, pygame
from model.Ship import Ship
from model.obstacle.enemy.Plane import Plane
from view import View

from src.model.Object import Object


class Game:
    stars = []
    ship = None
    HEIGHT = 10000
    WIDTH = 750

    def __init__(self, window):
        self.view = View(self, window)
        self.ship = Ship(self)
        self.objects = []
        self.spawn_objects()
        self.finished = False
        for i in range(1000):
            x = random.randrange(self.WIDTH)
            y = random.randrange(self.HEIGHT)
            size = random.randrange(2, 6)
            self.stars.append((x, y, size))

    def update(self, dt):
        self.ship.update(dt)
        for o in self.objects:
            o.update(dt)
        if self.ship.pos[1] > self.HEIGHT:
            self.finished = True

    def draw(self):
        self.view.window.fill((0, 0, 0))
        for (x, y, size) in self.stars:
            self.view.draw_image(x, y, Object.stars[size-2], 25, 25, 1)
            # self.view.draw_circle(x, y, (255, 255, 255), size)
        self.ship.draw()
        for o in self.objects:
            o.draw()

    def add_object(self, o):
        self.objects.append(o)

    def spawn_objects(self):
        # spawn some objects for demo purposes,
        plane = Plane(self)
        plane.set_pos(self.ship.pos + [0, 500])
        self.add_object(plane)
