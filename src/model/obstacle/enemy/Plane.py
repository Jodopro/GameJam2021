from model.obstacle.enemy.Enemy import Enemy


class Plane(Enemy):

    def __init__(self, game):
        super().__init__(game, color=(255,210,24), width=100, height=20)



    def get_hitbox(self):
        box = super().get_hitbox()
        return box