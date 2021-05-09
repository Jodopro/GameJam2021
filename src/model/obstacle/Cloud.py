import enum

from model.obstacle.Obstacle import Obstacle
import random

from model.obstacle.attack.Bliksem import Bliksem
from config import *
import numpy as np

from config import *

bliksem_delay = 0.7

class Cloud(Obstacle):
    class Type(enum.Enum):
        White = 1
        Grey = 2
        Black = 3

    type = Type(2) # default type

    def __init__(self, *args, game, delay=0.5, **kwargs):
        super().__init__(*args, game=game, width=2*46, height=2*30, **kwargs)
        temp_y = int((1 - BIRD_SPAWN_PLACE) * WINDOW_HEIGHT) + random.randrange(int(WINDOW_HEIGHT * BIRD_SPAWN_PLACE))
        y = game.ship.pos[1] - PLAYER_OFFSET + temp_y
        x = random.randrange(50, WINDOW_WIDTH-50)
        self.pos = np.array([x, y])
        self.delay = delay
        self.time_elapsed = 0.0
        self.bliksem = False


    def draw(self):
        if self.type == Cloud.Type.White:
            self.game.view.draw_image(self.pos[0], self.pos[1], CLOUD_WHITE, self.width, self.height)
        if self.type == Cloud.Type.Grey:
            self.game.view.draw_image(self.pos[0], self.pos[1], CLOUD_GREY, self.width, self.height)
        if self.type == Cloud.Type.Black:
            self.game.view.draw_image(self.pos[0], self.pos[1], CLOUD_BLACK, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox(), self.color)


    def update(self, d_t):
        super().update(d_t)
        self.time_elapsed += d_t
        if self.type == Cloud.Type.Grey:
            if self.time_elapsed >= self.delay:
                self.change_type()
        if self.type == Cloud.Type.Black:
            if self.time_elapsed >= bliksem_delay:
                if not self.bliksem:
                    self.make_bliksem()
                    self.bliksem = True
                # self.game.remove_object(self)

    def change_type(self):
        self.type = random.choice([Cloud.Type.White, Cloud.Type.Black])
        if self.type == Cloud.Type.Black:
            self.game.remove_object(self)
            self.nature = Obstacle.Nature.Hostile
            self.game.add_object(self)
            self.time_elapsed = 0.0

    def make_bliksem(self):
        self.game.add_object(Bliksem(self.game, origin=self.pos))

