import pygame
import numpy as np
from config import *
from board import draw_board

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dart Simulator")

pygame.font.init()
font_size = int(15 * SCALE)
font = pygame.font.SysFont("Arial", font_size, bold=True)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 30, 30))

    draw_board(screen, font)

    pygame.display.flip()

pygame.quit()