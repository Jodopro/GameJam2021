from model.obstacle.Obstacle import Obstacle


class Enemy(Obstacle):
    prop = None

    def __init__(self, *args, nature=Obstacle.Nature.Hostile, **kwargs):
        super().__init__(*args, nature=nature, **kwargs)