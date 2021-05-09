import pygame, numpy

# Debug settings
DRAW_HITBOX = False
PRINT_TIME = False

# Window settings
WINDOW_HEIGHT = 1000
WINDOW_WIDTH = 750

# Player settings
PLAYER_OFFSET = 100
PLAYER_MAX_SPEED = numpy.array([300.0, 400.0])
PLAYER_MIN_SPEED = numpy.array([-PLAYER_MAX_SPEED[0], 200.0])
PLAYER_SHOOTING_DELAY = 0.1

# Enemy settings
BIRD_SHOOTING_DELAY = 0.1

# Other settings
WAVE_SPEED = 500
WAVE_WIDTH_EXPANSION = 50

# Images
BACKGROUND_IMG = pygame.image.load("view/ugly_background2.png")
HOUSE_IMG = pygame.image.load("view/house.png")
BALLOON_IMG = pygame.image.load("view/balloon.png")
BIRD_IMG = pygame.image.load("view/spaceship.png")
BIRD_FLIP_IMG = pygame.transform.flip(BIRD_IMG, True, False)
WAVE_ENEMY_PNG = pygame.image.load("view/soundwave_purple.png")
WAVE_RAINBOW_PNG = pygame.image.load("view/soundwave_green.png")

