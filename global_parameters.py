import os
import pygame

class Parameters:

    # Defining the constants
    WINDOW_SIZE = (WIDTH, HEIGHT) = (1000, 500)
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # colors variables
    BLACK = (0, 0, 0)
    WHITE = (247, 247, 247)
    FONT_COLOR = (83, 83, 83)

    SCREEN_WIDTH = 60
    SCREEN_HEIGHT = 100

    IMAGE_PATH = "img/"

    SMALL_CACTUS = [
        pygame.image.load(os.path.join(
            IMAGE_PATH, "3. Obstacles/SmallCactus1.png")),
        pygame.image.load(os.path.join(
            IMAGE_PATH, "3. Obstacles/SmallCactus2.png")),
        pygame.image.load(os.path.join(
            IMAGE_PATH, "3. Obstacles/SmallCactus3.png")),
    ]

    LARGE_CACTUS = [
        pygame.image.load(os.path.join(
            IMAGE_PATH, "3. Obstacles/LargeCactus1.png")),
        pygame.image.load(os.path.join(
            IMAGE_PATH, "3. Obstacles/LargeCactus2.png")),
        pygame.image.load(os.path.join(
            IMAGE_PATH, "3. Obstacles/LargeCactus3.png")),
    ]

    BIRD = [
        pygame.image.load(os.path.join(IMAGE_PATH, "3. Obstacles/Bird1.png")),
        pygame.image.load(os.path.join(IMAGE_PATH, "3. Obstacles/Bird2.png"))
    ]

    # screen and background settings
    #bg_img = pygame.image.load("img/1.Background/DinoTrack.png")  # load the track image
    #bg_size = (bg_width, bg_height) = (bg_img.get_width(),
                                       #bg_img.get_height())
    #print(bg_size)
    # getting the track image size

    # implementing the logo and caption of the game
    logo = pygame.image.load(os.path.join(IMAGE_PATH, "1.Background/Logo.png"))

    isDead = False
    point = 0
    isRunnung = False
    firstTime = True
    themeOption = 0
    pointmax = 0



