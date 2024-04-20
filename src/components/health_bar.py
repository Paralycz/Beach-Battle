import pygame

class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x
        self.y = y
        self.hp = hp
        self.max_hp = max_hp

    def draw(self, screen, hp):
        self.hp = hp

        # Calculate Health Ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(screen, 'red', (self.x, self.y, 221, 10)) # last 2 paramets are width and height of rectangle
        pygame.draw.rect(screen, 'green', (self.x, self.y, 221*ratio, 10))