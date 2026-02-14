import pygame
from config import *

def aim_drawing(screen: pygame.Surface, pos: tuple, radius: int = 10):
    pygame.draw.circle(screen, (255, 0, 0), pos, int(3 * SCALE))
    pygame.draw.circle(screen, (0, 0, 0), pos, int(3 * SCALE), 1)