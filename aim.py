import pygame
from config import *

def aim_drawing(screen: pygame.Surface, pos: tuple, std_dev: float, radius: int = 10):
    pygame.draw.circle(screen, (255, 0, 0), pos, int(3 * SCALE))
    pygame.draw.circle(screen, (0, 0, 0), pos, int(3 * SCALE), 1)
    pygame.draw.circle(screen, (0, 0, 0), pos, int(SCALE * std_dev), 2)