import enum

from model.obstacle.Obstacle import Obstacle
import random

from model.obstacle.attack.Bliksem import Bliksem

bliksem_delay = 2.0

class Cloud(Obstacle):
    class Type(enum.Enum):
        White = 1
        Grey = 2
        Black = 3

    type = Type(2) # default type

    def __init__(self, *args, delay=2.0, **kwargs):
        super().__init__(*args, **kwargs)
        self.delay = delay
        self.time_elapsed = 0.0


    def draw(self):
        super().draw()
        # draw a cloud with appropriate color

    def update(self, d_t):
        super().update(d_t)
        self.time_elapsed += d_t
        if self.type == Cloud.Type.Grey:
            if self.time_elapsed >= self.delay:
                self.change_type()
        if self.type == Cloud.Type.Black:
            if self.time_elapsed >= bliksem_delay:
                self.make_bliksem()

    def change_type(self):
        self.type = random.choice([Cloud.Type.White, Cloud.Type.Black])
        if self.type == Cloud.Type.Black:
            self.nature = Obstacle.Nature.Hostile
            self.time_elapsed = 0.0

    def make_bliksem(self):
        self.game.add_object(Bliksem(self.game, origin=self.pos))

