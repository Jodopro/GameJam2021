from model.obstacle.attack.Attack import Attack


class Bliksem(Attack):
    def __init__(self, *args, **kwargs):
        # modify kwargs where necessary
        super().__init__(*args, **kwargs)
        # init other variables here