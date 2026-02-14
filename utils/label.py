import pygame

class Label:
    def __init__(self, text, pos, size=30, color=(255, 255, 255), font_name=None):
        # Jeśli font_name jest None, używa domyślnej czcionki systemowej
        self.font = pygame.font.SysFont(font_name, size)
        self.color = color
        self.pos = pos
        self.set_text(text)

    def set_text(self, text):
        """Renderuje tekst na powierzchni (Surface)"""
        self.image = self.font.render(str(text), True, self.color)
        # Ustawiamy pozycję na podstawie podanego lewego górnego rogu
        self.rect = self.image.get_rect(topleft=self.pos)

    def draw(self, surface):
        """Rysuje tekst na ekranie"""
        surface.blit(self.image, self.rect)