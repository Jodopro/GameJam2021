import numpy as np


class Object:
    pos = np.array([0.0,0.0])
    speed = np.array([0.0,0.0])

    def set_pos(self, new_position):
        self.pos = np.array(new_position)

    def set_speed(self, new_speed):
        self.speed = np.array(new_speed)

    def draw(self):
        pass

    def update(self, delta_t):
        self.pos += delta_t * self.speed