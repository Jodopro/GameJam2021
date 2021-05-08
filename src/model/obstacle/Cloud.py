import enum

from model.obstacle.Obstacle import Obstacle


class Cloud(Obstacle):
    class Type(enum.Enum):
        Passive = 1
        Neutral = 2
        Aggressive = 3

    type = Type(2) # default type


    def draw(self):
        super.draw()
        # subsequently, do your own drawing

    def update(self, delta_t):
        super().update(delta_t)
        # subsequently, do your own drawing
