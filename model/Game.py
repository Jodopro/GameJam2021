import random


class Game:
    player_y = 10
    player_x = 0
    player_dx = 0
    player_dy = 0
    stars = []

    def __init__(self):
        height = 1000
        width = 750
        for i in range(1000):
            x = random.randrange(width)
            y = random.randrange(height)
            self.stars.append((x, y))

    def update(self, dt):
        self.player_y += dt*self.player_dy
        self.player_x += dt*self.player_dx

    def draw_window(self, window):
        # window.
        for (x, y) in self.stars:
            temp_y = x-self.player_y
