import pygame

pygame.init()
pygame.font.init()
myFont = pygame.font.SysFont('Comic Sans MS', 25)
lobster = pygame.font.SysFont('Lobster Regular 400', 20)
screenWidth = 900
screenHeight = 650
screen = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 91, 0)
HZ = (100, 100, 100)
PINK = (250, 128, 114)
DARK_RED = (139, 0, 0)
VISION_COLOR = (0, 255, 127)