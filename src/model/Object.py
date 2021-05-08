import numpy as np


class Object:
    pos = np.array([0.0,0.0])
    speed = np.array([0.0,0.0])
    acc = np.array([0.0,0.0])

    def set_pos(self, new_position):
        self.pos = np.array(new_position)

    def set_speed(self, new_speed):
        self.speed = np.array(new_speed)

    def set_acc(self, new_acc):
        self.acc = np.array(new_acc)

    def draw(self):
        pass

    def update_speed(self, dt):
        self.speed += dt * self.acc

    def update_pos(self, dt):
        self.pos += dt * self.speed

    def update(self, dt):
        self.update_speed(dt)
        self.update_pos(dt)
