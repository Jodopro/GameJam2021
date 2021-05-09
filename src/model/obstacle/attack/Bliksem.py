from model.obstacle.attack.Attack import Attack


class Bliksem(Attack):
    def __init__(self, *args, origin, **kwargs):
        super().__init__(*args, direction=[0.0,-1.0], **kwargs)
        self.pos = origin.copy()
        # init other variables here