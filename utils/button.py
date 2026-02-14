import pygame

class Button:
    COLOR_INACTIVE = (100, 100, 100)
    COLOR_ACTIVE = (150, 150, 150)
    COLOR_TEXT = (255, 255, 255)

    def __init__(self, x, y, width, height, text, font_size=30, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont('Arial', font_size)
        self.action = action
        self.is_hovered = False

    def draw(self, surface):
        # Zmiana koloru w zależności od najechania myszką
        color = self.COLOR_ACTIVE if self.is_hovered else self.COLOR_INACTIVE
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        
        # Renderowanie tekstu
        text_surf = self.font.render(self.text, True, self.COLOR_TEXT)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def check_hover(self, mouse_pos):
        # Sprawdza czy myszka jest nad przyciskiem
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        # Sprawdza kliknięcie
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.is_hovered and self.action:
                self.action()