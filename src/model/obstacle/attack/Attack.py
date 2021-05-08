from model.Object import Object
from model.obstacle.Obstacle import Obstacle


class Attack(Obstacle):
    def __init__(self, game):
        super().__init__(game)