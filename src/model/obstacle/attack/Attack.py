from model.Object import Object
from model.obstacle.Obstacle import Obstacle


class Attack(Obstacle):
    def __init__(self, *args, nature=Obstacle.Nature.Hostile, speed, origin,  **kwargs):
        super().__init__(*args, nature=nature, **kwargs)
        self.pos = origin.copy()
        self.speed = speed.copy()