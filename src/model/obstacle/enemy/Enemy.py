from model.Explosion import Explosion
from model.obstacle.Obstacle import Obstacle


class Enemy(Obstacle):
    prop = None

    def __init__(self, *args, nature=Obstacle.Nature.Hostile, **kwargs):
        super().__init__(*args, nature=nature, **kwargs)
        self.hit=False

    def get_hit(self):
        self.game.replace_object(self, Explosion(self.game, origin=self.pos))

    def update(self, dt):
        super().update(dt)


