from config import *


class BatteryDisplayer:
    def __init__(self, game):
        self.game = game

    def draw(self):
        percentage = self.game.ship.battery*100/PLAYER_BATTERY_SIZE
        image = None
        for (p, i) in BATTERY_ARRAY:
            if percentage < p:
                break
            image = i
        y = (self.game.ship.pos[1]-PLAYER_OFFSET) + WINDOW_HEIGHT*0.05
        self.game.view.draw_image(WINDOW_WIDTH*0.9, y, image, 100, 40, direction=[0, 1])
