import pygame, random

PLAYER_OFFSET = 100
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 750


class View:
    def __init__(self, game, window):
        self.game = game
        self.window = window

    def transform_y(self, y):
        return WINDOW_HEIGHT - PLAYER_OFFSET - (y - self.game.ship.pos[1])

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
            w_2 = width//2
            h_2 = height//2
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
        image = pygame.transform.scale(image, (width*scale, height*scale))
        rect = pygame.Rect(self.transform_x(x), self.transform_y(y), width, height)
        pygame.Surface.blit(self.window, image, rect)
