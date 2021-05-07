import random, pygame
from src.model.Ship import Ship


class Game:
    stars = []
    ship = None
    HEIGHT = 10000
    WIDTH = 750
    WINDOW_HEIGHT = 1000
    WINDOW_WIDTH = 750

    def __init__(self):
        self.ship = Ship(self)
        for i in range(1000):
            x = random.randrange(self.WIDTH)
            y = random.randrange(self.HEIGHT)
            size = random.randrange(2, 6)
            self.stars.append((x, y, size))

    def update(self, dt):
        self.ship.update(dt)

    def draw(self, window):
        window.fill((0, 0, 0))
        for (x, y, size) in self.stars:
            temp_y = y-self.ship.player_y
            pygame.draw.circle(window, (255, 255, 255), (x, self.WINDOW_HEIGHT-temp_y), size)
        self.ship.draw(window)
