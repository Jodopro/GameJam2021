from model.obstacle.attack.Attack import Attack
from config import *
import numpy as np

class Bliksem(Attack):
    def __init__(self, *args, origin, speed=np.array([0.0,0.0]), **kwargs):
        super().__init__(*args, speed=speed, origin=origin, direction=[0.0,-1.0], width=20, height=100, **kwargs)
        # self.pos = origin.copy()
        self.speed = np.array(self.direction) * BLIKSEM_SPEED


        # init other variables here


    def draw(self):
        self.game.view.draw_image(self.pos[0], self.pos[1], BLIKSEM, self.width, self.height)