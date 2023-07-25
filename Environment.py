import pygame
from pygame.locals import *
import time

HEIGHT = 600
WIDTH = 600
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
START = 0
PLAY = 1
FAIL = 2
SUCCESS = 3
QUIT = 4

pygame.init()

Font_24 = pygame.font.SysFont('方正粗黑宋简体', 24, False, False)
Font_48 = pygame.font.SysFont('方正粗黑宋简体', 48, False, False)