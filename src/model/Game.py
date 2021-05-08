import random
from model.Ship import Ship
from model.Ship import max_speed as ship_max_speed
from model.Ship import min_speed as ship_min_speed
from model.obstacle.enemy.Plane import Plane
from view import View
from view import WINDOW_HEIGHT

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
        garbage = []
        for o in self.objects:
            o.update(dt)
            if (o.pos[0] < -0.5*self.WIDTH) or (o.pos[0] > 1.5*self.WIDTH):
                garbage.append(o)
            elif (o.pos[1] < self.ship.pos[1] - (WINDOW_HEIGHT*0.5)) and (o.speed[1] < ship_min_speed[1]):
                garbage.append(o)
            elif (o.pos[1] > self.ship.pos[1] + (WINDOW_HEIGHT*1.5)) and (o.speed[1] > ship_max_speed[1]):
                garbage.append(o)
        for o in garbage:
            self.objects.remove(o)
            del o
        if self.ship.pos[1] > self.HEIGHT:
            self.finished = True

    def draw(self):
        self.view.window.fill((0, 0, 0))
        for (x, y, size) in self.stars:
            self.view.draw_image(x, y, Object.stars[size-2], 25, 25, 1)
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
