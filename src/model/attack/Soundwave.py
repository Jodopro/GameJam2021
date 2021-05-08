from src.model.attack.Attack import Attack

wave_speed = 500
width_expansion = 50

class Soundwave(Attack):
    def __init__(self, game, origin, speed, direction):
        self.game = game
        self.pos = origin.copy()
        self.speed = speed.copy()
        factor = (1/(direction[0]**2 + direction[1]**2))**0.5
        self.direction = factor*direction
        self.speed += self.direction*wave_speed
        self.width = 10

    def draw(self):
        self.game.view.draw_rect(self.pos[0], self.pos[1], (0, 255, 0), self.width, 10, self.direction)

    def update(self, dt):
        super().update(dt)
        self.width += dt * width_expansion
