import enum

from model.obstacle.Obstacle import Obstacle


class Cloud(Obstacle):
    class Type(enum.Enum):
        White = 1
        Grey = 2
        Black = 3

    type = Type(2) # default type


    def draw(self):
        super().draw()
        # subsequently, do your own drawing

    def update(self, delta_t):
        super().update(delta_t)
        # subsequently, do your own drawing
