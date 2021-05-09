import util, time
from config import *
from model.obstacle.Balloon import Balloon
from model.obstacle.Ship import Ship
from model.obstacle.Obstacle import Obstacle
from model.obstacle.enemy.Plane import Plane
from model.obstacle.attack.Soundwave import Soundwave
from model.Battery import Battery
from view import View

from model.obstacle.enemy.Bird import Bird


class Game:
    ship = None

    def __init__(self, window):
        self.start_time = time.time()
        self.score = 0
        self.enemy_spawning_delay = BIRD_SPAWNING_DELAY_START
        self.view = View(self, window)
        self.ship = Ship(self)
        self.objects = []
        self.hostile_obstacles = []
        self.neutral_obstacles = []
        self.friendly_obstacles = []
        self.add_object(self.ship)
        # todo: find out all pairs of colliding objects, and check for all collisions what needs to happen
        #   for most collisions, just remove both, but house can be hit by attacks, but not by enemies.
        #   balloon cannot be hit by any hostile obstacle!
        # self.spawn_objects()
        self.finished = False
        self.spawning_counter = 0
        self.battery = Battery(self)

    def update_spawner(self, dt):
        self.spawning_counter += dt
        if self.spawning_counter >= self.enemy_spawning_delay:
            self.enemy_spawning_delay *= BIRD_SPAWNING_DELAY_UPDATE_PERCENTAGE
            bird = Bird(self)
            self.add_object(bird)
            self.spawning_counter = 0

    def update(self, dt):
        self.update_spawner(dt)
        # self.ship.update(dt)
        garbage = []
        for o in self.objects:
            o.update(dt)
            if (o.pos[0] < -0.1 * WINDOW_HEIGHT) or (o.pos[0] > 1.1 * WINDOW_WIDTH):
                garbage.append(o)
            elif (o.pos[1] < self.ship.pos[1] - (WINDOW_HEIGHT * 0.1)) and (o.speed[1] < PLAYER_MIN_SPEED[1]):
                garbage.append(o)
            elif (o.pos[1] > self.ship.pos[1] + (WINDOW_HEIGHT * 1.1)) and (o.speed[1] > PLAYER_MAX_SPEED[1]):
                garbage.append(o)
        self.check_collisions()
        for o in garbage:
            self.remove_object(o)
            del o

    def check_collisions(self):
        colliding_indices = util.detect_collision_pairs(list(map(lambda o: o.get_hitbox(), self.friendly_obstacles)),
                                                      list(map(lambda o: o.get_hitbox(),
                                                               self.hostile_obstacles)))  # to collect all colliding pairs
        # for f_o in self.friendly_obstacles:
        #     for h_o in self.hostile_obstacles:
        #         if self.collision(f_o, h_o):
        #             colliding_pairs.append((f_o, h_o))
        #             f_o.color = (255, 0, 0)
        #             h_o.color = (255, 0, 0)
        # todo: don't calculate for every, pair, but do this dynamically in util.
        #   first, calculate all edge perps, then look at the collisions per f_o with all h_o's.
        # print(colliding_indices)
        colliding_pairs = []
        for i, j in colliding_indices:
            f_o = self.friendly_obstacles[i]
            h_o = self.hostile_obstacles[j]
            colliding_pairs.append((f_o, h_o))
        for (friendly, enemy) in colliding_pairs:
            if isinstance(friendly, Balloon):
                if CAN_DIE:
                    self.score = time.time() - self.start_time
                    self.finished = True
                else:
                    print("af")
            elif isinstance(friendly, Soundwave):
                self.remove_object(friendly)
                del friendly
            if isinstance(enemy, Soundwave):
                self.remove_object(enemy)
                del enemy
            # for o in c_p:
            #     o.color = (255, 0, 0)
                # if not isinstance(o, Ship) and not isinstance(o, Balloon):
                #     self.remove_object(o)
    # print(f'colliding pairs: {colliding_pairs}')
    # print(f'friendly obstacles: {self.friendly_obstacles}')
    # print(f'hostile obstacles: {self.hostile_obstacles}')
    # for o in self.objects:
    #     if isinstance(o, Obstacle):
    #         if self.collision(o):
    #             o.color = (255, 0, 0)


    def draw(self):
        self.view.window.fill((0, 0, 0))
        self.view.draw_background()
        for o in self.objects:
            o.draw()
        self.battery.draw()

    def add_object(self, o):
        self.objects.append(o)
        if isinstance(o, Ship):
            self.add_object(o.balloon)
        if isinstance(o, Obstacle):
            self.add_obstacle(o)


    def remove_object(self, o):
        try:
            self.objects.remove(o)
        except ValueError as e:
            return
        if isinstance(o, Obstacle):
            self.remove_obstacle(o)


    def add_obstacle(self, o):
        if o.nature == Obstacle.Nature.Friendly:
            self.friendly_obstacles.append(o)
        elif o.nature == Obstacle.Nature.Neutral:
            self.neutral_obstacles.append(o)
        elif o.nature == Obstacle.Nature.Hostile:
            self.hostile_obstacles.append(o)


    def remove_obstacle(self, o):
        if o.nature == Obstacle.Nature.Friendly:
            self.friendly_obstacles.remove(o)
        elif o.nature == Obstacle.Nature.Neutral:
            self.neutral_obstacles.remove(o)
        elif o.nature == Obstacle.Nature.Hostile:
            self.hostile_obstacles.remove(o)


    def spawn_objects(self):
        # spawn some objects for demo purposes,
        plane = Plane(self)
        plane.set_pos(self.ship.pos + [0, 500])
        self.add_object(plane)


    def collision(self, o1, o2):
        return util.detect_collision(o1.get_hitbox(), o2.get_hitbox())
