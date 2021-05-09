import numpy as np
from model.obstacle.Obstacle import Obstacle
from model.obstacle.attack.Soundwave import Soundwave
from model.obstacle.Balloon import Balloon
from config import *
from pygame import mixer
mixer.init()
mixer.music.load("Panzerkampf.mp3")
mixer.music.set_volume(1)


class Ship(Obstacle):

    def __init__(self, game, nature=Obstacle.Nature.Friendly):
        super().__init__(game, nature=nature)
        mixer.music.play()
        mixer.music.pause()
        self.width = 50
        self.height = 75
        self.set_pos([375.0, 100.0])
        self.set_speed([0.0, PLAYER_MIN_SPEED[1]])
        self.acc = np.array([0,0])
        self.shooting = False
        self.shooting_counter = PLAYER_SHOOTING_DELAY
        self.balloon = Balloon(game, self)

    def get_hitbox(self):
        a = self.pos + [-self.width/2, self.height/2]
        b = self.pos + [self.width/2, self.height/2]
        c = self.pos + [self.width/2, -self.height/2]
        d = self.pos + [-self.width/2, -self.height/2]
        return np.array([a,b,c,d])

    def update_speed(self, dt):
        super().update_speed(dt)
        for i in range(len(self.speed)):
            if self.speed[i] > PLAYER_MAX_SPEED[i]:
                self.speed[i] = PLAYER_MAX_SPEED[i]
            if self.speed[i] < PLAYER_MIN_SPEED[i]:
                self.speed[i] = PLAYER_MIN_SPEED[i]

    def update_shooting(self, dt):
        self.shooting_counter += dt
        if self.shooting_counter >= PLAYER_SHOOTING_DELAY:
            self.shooting_counter = PLAYER_SHOOTING_DELAY
            if self.shooting:
                if self.battery > 0:
                    mouse_loc = pygame.mouse.get_pos()
                    rel_x = mouse_loc[0]-self.pos[0]
                    rel_y = self.game.view.transform_y(self.pos[1]) - mouse_loc[1]
                    direction = np.array([rel_x, rel_y])
                    new_wave = Soundwave(self.game, origin=self.pos, speed=self.speed, direction=direction, nature=Obstacle.Nature.Friendly)
                    self.game.add_object(new_wave)
                    self.shooting_counter = 0
                else:
                    self.stop_shooting()

    def update_pos(self, dt):
        self.pos += dt * self.speed
        if self.pos[0] < 0 + self.width//2:
            self.pos[0] = 0 + self.width//2
            self.speed[0] = 0
        elif self.pos[0] > WINDOW_WIDTH - self.width//2:
            self.pos[0] = WINDOW_WIDTH - self.width//2
            self.speed[0] = 0

    def update(self, dt):
        super().update(dt)
        self.update_shooting(dt)
        self.balloon.update(dt)

    def draw(self):
        self.game.view.draw_image(self.pos[0], self.pos[1], HOUSE_IMG, self.width, self.height)
        self.game.view.draw_hitbox(self.get_hitbox())
        self.balloon.draw()
