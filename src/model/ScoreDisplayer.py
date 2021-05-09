from config import *
import time


class ScoreDisplayer:
    def __init__(self, game):
        self.game = game

    def draw(self):
        score = '%.2f' % (time.time() - self.game.start_time)
        y = (self.game.ship.pos[1]-PLAYER_OFFSET) + WINDOW_HEIGHT*0.075
        self.game.view.draw_text(WINDOW_WIDTH*0.05, y, score)
