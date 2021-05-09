import pygame, numpy

# Debug settings
DRAW_HITBOX = False
PRINT_TIME = False

# Window settings
WINDOW_HEIGHT = 750
WINDOW_WIDTH = 500

# Player settings
PLAYER_OFFSET = 100
PLAYER_MAX_SPEED = numpy.array([300.0, 400.0])
PLAYER_MIN_SPEED = numpy.array([-PLAYER_MAX_SPEED[0], 200.0])
PLAYER_SHOOTING_DELAY = 0.1
PLAYER_BATTERY_SIZE = 100
PLAYER_BATTERY_CHARGE = 25
PLAYER_BATTERY_CONSUME = 25
PLAYER_BATTERY_MINIMUM_FACTOR = 0.1

# Enemy settings
BIRD_SHOOTING_DELAY = 0.1
BIRD_BURST = 3
BIRD_BURST_WAIT = 3
BIRD_SPAWNING_DELAY_START = 1
BIRD_SPAWNING_DELAY_UPDATE_PERCENTAGE = 0.99

# Other settings
WAVE_SPEED = 500
WAVE_WIDTH_EXPANSION = 50

# Images
BACKGROUND_IMG = pygame.image.load("view/ugly_background2.png")
HOUSE_IMG = pygame.image.load("view/house.png")  # replace with "view/police_box.png" for a cool B-skin B)
BALLOON_IMG = pygame.image.load("view/balloon.png")
BIRD_IMG = pygame.image.load("view/spaceship.png")
BIRD_FLIP_IMG = pygame.transform.flip(BIRD_IMG, True, False)
WAVE_ENEMY_PNG = pygame.image.load("view/soundwave_purple.png")
WAVE_RAINBOW_PNG = pygame.image.load("view/soundwave_green.png")
BATTERY_EMPTY = pygame.image.load("view/battery_empty")
BATTERY_25 = pygame.image.load("view/battery_25y")
BATTERY_50 = pygame.image.load("view/battery_50")
BATTERY_75 = pygame.image.load("view/battery_75")
BATTERY_FULL= pygame.image.load("view/battery_fully")
BATTERY_ARRAY = [BATTERY_EMPTY, BATTERY_25, BATTERY_50, BATTERY_75, BATTERY_FULL]

