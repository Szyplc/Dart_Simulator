import math
from config import *
import pygame

def get_sector_polygon(start_angle: float, end_angle: float, r_inner: float, r_outer: float, segments: int = 10):
    """Oblicza punkty dla wycinka pierścienia (trapezoidalny kształt)."""
    points = []
    # Zewnętrzny łuk
    for i in range(segments + 1):
        angle = math.radians(start_angle + (end_angle - start_angle) * i / segments)
        points.append((CENTER[0] + r_outer * math.sin(angle), 
                       CENTER[1] - r_outer * math.cos(angle)))
    # Wewnętrzny łuk (od tyłu)
    for i in range(segments, -1, -1):
        angle = math.radians(start_angle + (end_angle - start_angle) * i / segments)
        points.append((CENTER[0] + r_inner * math.sin(angle), 
                       CENTER[1] - r_inner * math.cos(angle)))
    return points


def draw_board(screen: pygame.Surface, font: pygame.font.Font):
    for i in range(20):
        start_angle = -9 + i * 18
        end_angle = start_angle + 18
        
        # Kolory naprzemienne
        main_color = WHITE if i % 2 != 0 else BLACK
        sec_color = RED if i % 2 == 0 else GREEN

        # 1. Główny duży wycinek (Single)
        # Część wewnętrzna (między Triple a Bullseye)
        p2 = get_sector_polygon(start_angle, end_angle, R_BULL_OUT, R_TRIPLE_IN)
        pygame.draw.polygon(screen, main_color, p2)

        # 2. Pierścień Triple
        p_triple = get_sector_polygon(start_angle, end_angle, R_TRIPLE_IN, R_TRIPLE_OUT)
        pygame.draw.polygon(screen, sec_color, p_triple)

        # 3. Część zewnętrzna (między Double a Triple)
        p1 = get_sector_polygon(start_angle, end_angle, R_TRIPLE_OUT, R_DOUBLE_IN)
        pygame.draw.polygon(screen, main_color, p1)
        
        # 4. Pierścień Double
        p_double = get_sector_polygon(start_angle, end_angle, R_DOUBLE_IN, R_DOUBLE_OUT)
        pygame.draw.polygon(screen, sec_color, p_double)


    # 5. Bullseye
    pygame.draw.circle(screen, GREEN, CENTER, int(R_BULL_OUT))
    pygame.draw.circle(screen, RED, CENTER, int(R_BULL_IN))

    # 6. Obramowanie
    pygame.draw.circle(screen, BLACK, CENTER, int(R_DOUBLE_OUT + 20 * SCALE), int(20 * SCALE))
    
    R_NUMBERS = R_DOUBLE_OUT + (12 * SCALE)
    for i in range(20):
        # Kąt dla każdej liczby (środek sektora)
        # i * 18 stopni daje nam środek każdego pola
        angle_deg = i * 18
        angle_rad = math.radians(angle_deg)
        
        # Obliczenie pozycji (x, y)
        x = CENTER[0] + R_NUMBERS * math.sin(angle_rad)
        y = CENTER[1] - R_NUMBERS * math.cos(angle_rad)
        
        # Pobranie wartości z tablicy punktacji
        number_text = str(BOARD_VALUES[i])
        text_surface = font.render(number_text, True, WHITE)
        
        # Wyśrodkowanie tekstu (bounding box)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)