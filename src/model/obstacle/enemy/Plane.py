from model.obstacle.enemy.Enemy import Enemy


class Plane(Enemy):

    def __init__(self, game):
        super().__init__(game)
        self.color = (255, 210, 24) # mooiste kleur in het universum
        self.width = 100
        self.height = 20

    def draw(self):
        self.game.view.draw_rect(self.pos[0], self.pos[1], self.color, self.width, self.height)
