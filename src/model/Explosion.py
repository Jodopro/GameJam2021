from config import *
from model.obstacle.Obstacle import Obstacle


class Explosion(Obstacle):
    def __init__(self, *args, origin, duration=0.5, **kwargs):
        super().__init__(*args, nature=Obstacle.Nature.Hostile, **kwargs)
        self.pos = origin.copy()
        self.time_elapsed = 0.0 # seconds
        self.duration = duration

    def update(self, dt):
        super().update(dt)
        self.time_elapsed += dt
        if self.time_elapsed >= self.duration:
            self.game.remove_object(self)

    def draw(self):
        self.game.view.draw_image(self.pos[0], self.pos[1], EXPLOSION, self.width, self.height)