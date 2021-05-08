from src.model.attack.Attack import Attack

wave_speed = 500

class Soundwave(Attack):
    def __init__(self, game, origin, speed, direction):
        self.game = game
        self.pos = origin.copy()
        self.speed = speed.copy()
        normalize_factor = (wave_speed**2/(direction[0]**2 + direction[1]**2))**0.5
        self.speed += normalize_factor*direction

    def draw(self):
        self.game.view.draw_circle(self.pos[0], self.pos[1], (0, 255, 0), 5)