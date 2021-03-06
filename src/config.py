import pygame, numpy, random

# Debug settings
DRAW_HITBOX = False
PRINT_TIME = False
CAN_DIE = True

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
BIRD_SPAWN_PLACE = 0.25
BIRD_SHOOTING_DELAY = 0.1
BIRD_BURST = 2
BIRD_BURST_WAIT = 4
BIRD_SPAWNING_DELAY = 1
BIRD_SPAWNING_DELAY_DECREASE = 0.99
BLIKSEM_SPEED = 900


# Other settings
DIFFICULTY_INCREASE = 1
FONT = pygame.font.SysFont(None, 48)
WAVE_SPEED = 500
WAVE_WIDTH_EXPANSION = 50

# Images
BACKGROUND_IMG = pygame.image.load("view/background_sky.png")
BACKGROUND_IMG_STARS = pygame.image.load("view/ugly_background.png")
HOUSE_IMG = pygame.image.load("view/house_2.png")
POLICE_BOX = pygame.image.load("view/police_box.png")
POLICE_BOX_SHINY = pygame.image.load("view/police_box_shiny.png")
# HOUSE_IMG = POLICE_BOX_SHINY
BALLOON_IMG = pygame.image.load("view/balloon.png")
RANDOM_BIRD_IMG = pygame.image.load("view/spaceship_green.png")
RANDOM_BIRD_FLIP_IMG = pygame.transform.flip(RANDOM_BIRD_IMG, True, False)
CONSTANT_BIRD_IMG = pygame.image.load("view/spaceship_red.png")
CONSTANT_BIRD_FLIP_IMG = pygame.transform.flip(CONSTANT_BIRD_IMG, True, False)
AIMED_BIRD_IMG = pygame.image.load("view/spaceship_purple.png")
AIMED_BIRD_FLIP_IMG = pygame.transform.flip(AIMED_BIRD_IMG, True, False)
WAVE_ENEMY_PNG = pygame.image.load("view/soundwave_black.png")
WAVE_RAINBOW_PNG = pygame.image.load("view/soundwave_house.png")
BATTERY_EMPTY = pygame.image.load("view/battery_empty.png")
BATTERY_10 = pygame.image.load("view/battery_10.png")
BATTERY_20 = pygame.image.load("view/battery_20.png")
BATTERY_30 = pygame.image.load("view/battery_30.png")
BATTERY_40 = pygame.image.load("view/battery_40.png")
BATTERY_50 = pygame.image.load("view/battery_50.png")
BATTERY_60 = pygame.image.load("view/battery_60.png")
BATTERY_70 = pygame.image.load("view/battery_70.png")
BATTERY_80 = pygame.image.load("view/battery_80.png")
BATTERY_90 = pygame.image.load("view/battery_90.png")
BATTERY_100 = pygame.image.load("view/battery_100.png")
BATTERY_FULL = pygame.image.load("view/battery_full.png")
BATTERY_ARRAY = [
    (0, BATTERY_EMPTY),
    (10, BATTERY_10),
    (20, BATTERY_20),
    (30, BATTERY_30),
    (40, BATTERY_40),
    (50, BATTERY_50),
    (60, BATTERY_60),
    (70, BATTERY_70),
    (80, BATTERY_80),
    (90, BATTERY_90),
    (100, BATTERY_100)]
EXPLOSION = pygame.image.load("view/splooooooosion.png")

# Sound waves
BLACK_WAVE = pygame.image.load("view/soundwave_black.png")
BLUE_WAVE = pygame.image.load("view/soundwave_blue.png")
GREEN_WAVE = pygame.image.load("view/soundwave_green.png")
GREY_WAVE = pygame.image.load("view/soundwave_grey.png")
WHITE_WAVE = pygame.image.load("view/soundwave_house.png")
ORANGE_WAVE = pygame.image.load("view/soundwave_orange.png")
PINK_WAVE = pygame.image.load("view/soundwave_pink.png")
PURPLE_WAVE = pygame.image.load("view/soundwave_purple.png")
RED_WAVE = pygame.image.load("view/soundwave_red.png")
YELLOW_WAVE = pygame.image.load("view/soundwave_yellow.png")
WAVE_ARRAY = [BLACK_WAVE, BLUE_WAVE, GREEN_WAVE, GREY_WAVE, WHITE_WAVE, ORANGE_WAVE, PINK_WAVE, PURPLE_WAVE, RED_WAVE, YELLOW_WAVE]

CLOUD_WHITE = pygame.image.load("view/cloud.png")
CLOUD_GREY = pygame.image.load("view/cloud_grey.png")
CLOUD_BLACK = pygame.image.load("view/cloud_black.png")
BLIKSEM = pygame.image.load("view/lightning.png")