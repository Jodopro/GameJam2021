from model.obstacle.Obstacle import Obstacle


class Policebox(Obstacle):
    def __init__(self, *args, nature=Obstacle.Nature.Neutral, **kwargs):
        super().__init__(*args, nature=nature, **kwargs)