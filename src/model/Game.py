import util
from model.obstacle.Ship import Ship
from model.obstacle.Ship import max_speed as ship_max_speed
from model.obstacle.Ship import min_speed as ship_min_speed
from model.obstacle.Obstacle import Obstacle
from model.obstacle.enemy.Plane import Plane
from view import View

from model.obstacle.enemy.Bird import Bird

game_height = 10000
spawning_delay = 1


class Game:
    ship = None

    def __init__(self, window):
        self.view = View(self, window)
        self.ship = Ship(self)
        self.objects = []
        self.spawn_objects()
        self.finished = False
        width, height = window.get_size()
        self.window_width = width
        self.window_height = height
        self.spawning_counter = 0

    def update_spawner(self, dt):
        self.spawning_counter += dt
        if self.spawning_counter >= spawning_delay:
            bird = Bird(self)
            self.add_object(bird)
            self.spawning_counter = 0

    def update(self, dt):
        self.update_spawner(dt)
        self.ship.update(dt)
        garbage = []
        for o in self.objects:
            o.update(dt)
            if (o.pos[0] < -0.1*self.window_width) or (o.pos[0] > 1.1*self.window_width):
                garbage.append(o)
            elif (o.pos[1] < self.ship.pos[1] - (self.window_height*0.1)) and (o.speed[1] < ship_min_speed[1]):
                garbage.append(o)
            elif (o.pos[1] > self.ship.pos[1] + (self.window_height*1.1)) and (o.speed[1] > ship_max_speed[1]):
                garbage.append(o)
        self.check_collisions()
        for o in garbage:
            self.objects.remove(o)
            del o

        if self.ship.pos[1] > game_height:
            self.finished = True

    def check_collisions(self):
        for o in self.objects:
            if isinstance(o, Obstacle):
                if self.collision(o):
                    o.color = (255,0,0)

    def draw(self):
        self.view.window.fill((0, 0, 0))
        self.view.draw_background()
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

    def collision(self, obstacle):
        return util.detect_collision(self.ship.get_hitbox(), obstacle.get_hitbox())