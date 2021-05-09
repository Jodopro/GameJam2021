from model.Object import Object
from model.obstacle.Obstacle import Obstacle


class Attack(Obstacle):
    def __init__(self, *args, nature=Obstacle.Nature.Hostile, **kwargs):
        super().__init__(*args, nature=nature, **kwargs)