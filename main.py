import pygame
import numpy as np
from config import *
from board import draw_board
from aim import aim_drawing
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from score_evaluation import evaluate_score
from utils.label import Label
from utils.button import Button

pygame.init()

screen = pygame.display.set_mode((WIDTH + CONFIG_WIDTH, HEIGHT))
pygame.display.set_caption("Dart Simulator")

pygame.font.init()
font_size = int(15 * SCALE)
font = pygame.font.SysFont("Arial", font_size, bold=True)

aim = None

title_label = Label("Symulacja", (WIDTH + 20, 20), size=40, color=(0, 255, 200))

std_dev = 50
std_dev_label = Label("Odchylenie standardowe", (WIDTH + 20, 100), size=30, color=(255, 255, 255))
slider = Slider(screen, WIDTH + 25, 150, 200, 20, min=0, max=100, step=1, initial=std_dev)
output = TextBox(screen, WIDTH + 275, 140, 100, 40, 
                    fontSize=25, 
                    textColor=(0, 0, 0),
                    onColor=(255, 255, 255),
                    inactiveColour=(230, 230, 230),
                    radius=5
                )

throws_count = None
throws_label = Label("Liczba rzutów", (WIDTH + 25, 210), size=30, color=(255, 255, 255))
throws = TextBox(screen, WIDTH + 275, 200, 100, 40,
                    fontSize=25, 
                    textColor=(0, 0, 0),
                    onColor=(255, 255, 255),
                    inactiveColour=(230, 230, 230),
                    radius=5
                )


def on_button_click():
    r = np.random.normal(loc=0, scale=std_dev, size=throws_count)
    phi = np.random.uniform(0, 2 * np.pi, size=throws_count)
    for i in range(throws_count):
        x = aim[0] + r[i] * np.cos(phi[i])
        y = aim[1] + r[i] * np.sin(phi[i])
        score = evaluate_score((x, y))
        print(f"Rzut {i+1}: ({x:.2f}, {y:.2f}) - Punkty: {score}")
        


my_button = Button(WIDTH + 25, 250, 100, 30, "Start", action=on_button_click)

running = True
while running:
    screen.fill((30, 30, 30))
    draw_board(screen, font)
    pygame.draw.line(screen, (255, 255, 255), (WIDTH, 0), (WIDTH, HEIGHT), 2)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0] <= WIDTH:
                    aim = pos
                    score = evaluate_score(pos)
        
        my_button.handle_event(event)

    mouse_pos = pygame.mouse.get_pos()
    my_button.check_hover(mouse_pos)
    my_button.draw(screen)
    
    pygame_widgets.update(events)

    std_dev = slider.getValue()
    output.setText(str(std_dev))
    
    try:
        throws_count = int(throws.getText())
    except ValueError:
        throws_count = 0

    title_label.draw(screen)
    std_dev_label.draw(screen)
    throws_label.draw(screen)

    if aim:
        aim_drawing(screen, aim)

    pygame.display.flip()

pygame.quit()