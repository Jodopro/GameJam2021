import pygame
import numpy as np

PLAYER_OFFSET = 100
BACKGROUND_IMG = pygame.image.load("view/ugly_background2.png")


class View:
    def __init__(self, game, window):
        width, height = window.get_size()
        self.window_width = width
        self.window_height = height
        self.game = game
        self.window = window

    def transform_y(self, y):
        return self.window_height - PLAYER_OFFSET - (y - self.game.ship.pos[1])

    def transform_x(self, x):
        return x

    def draw_circle(self, x, y, color, radius):
        """
        draw a circle based on in-game coordinates
        :param x: in-game x position of the center of the circle
        :param y: in-game y position of the center of the circle
        :param color: color of the circle
        :param radius: radius of the circle
        :return:
        """
        pygame.draw.circle(self.window, color, (self.transform_x(x), self.transform_y(y)), radius)

    def draw_rect(self, x, y, color, width, height, direction=[1, 0]):
        """
        draw a rectangle based on in-game coordinates
        :param x: in-game x position of the center of the rectangle
        :param y: in-game y position of the center of the rectangle
        :param color: color of the rectangle expressed as an int three-tuple: (r, g, b)
        :param width: width of the rectangle
        :param height: height of the rectangle
        :param direction: unit vector of the direction, [sin(angle), cos(angle)]
        :return:
        """
        if direction[0] == 1 and direction[1] == 0:
            pygame.draw.rect(self.window, color,
                             (self.transform_x(x) - width // 2, self.transform_y(y) - height // 2, width, height))
        else:
            t_x = self.transform_x(x)
            t_y = self.transform_y(y)
            w_2 = width // 2
            h_2 = height // 2
            posses = [
                (-w_2, -h_2),
                (w_2, -h_2),
                (w_2, h_2),
                (-w_2, h_2),
            ]
            sin_angle = direction[0]
            cos_angle = direction[1]
            new_posses = []
            for (p_x, p_y) in posses:
                x_new = p_x * cos_angle - p_y * sin_angle
                y_new = p_x * sin_angle + p_y * cos_angle
                new_posses.append((t_x + x_new, t_y + y_new))
            pygame.draw.polygon(self.window, color, new_posses)

    def draw_image(self, x, y, image, width, height, scale):
        t_width = width * scale
        t_height = height * scale
        if scale != 1:
            image = pygame.transform.scale(image, (t_width, t_height))
        rect = pygame.Rect(self.transform_x(x) - t_width // 2, self.transform_y(y), t_width, t_height)
        pygame.Surface.blit(self.window, image, rect)

    def draw_background(self):
        offset = self.game.ship.pos[1] % 200
        y = offset - 200
        for i in range(11):
            rect = pygame.Rect(0, y, 750, 200)
            pygame.Surface.blit(self.window, BACKGROUND_IMG, rect)
            y += 200

    def draw_hitbox(self, box):
        edges = list(zip(box, np.append(box[1:], [box[0]], axis=0)))
        for e in edges:
            for pos in e:
                pos[0] = self.transform_x(pos[0])
                pos[1] = self.transform_y(pos[1])
            pygame.draw.line(self.window, (255, 0, 0), e[0], e[1])
