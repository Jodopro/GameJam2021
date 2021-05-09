from model.obstacle.attack.Attack import Attack
from config import *

class Bliksem(Attack):
    def __init__(self, *args, origin, **kwargs):
        super().__init__(*args, direction=[0.0,-1.0], **kwargs)
        self.pos = origin.copy()
        self.speed = self.speed * BLIKSEM_SPEED


        # init other variables here


    def draw(self):
        pass # draw bliksem image