import pygame

from src.services.visualization_service import VisualizationServices


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color):
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        self.image = VisualizationServices.get_font(30).render(str(damage), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.counter = 0

    def update(self):
        self.rect.y -= 1
        
		#delete the text after a few seconds
        self.counter += 1

        if self.counter > 30:
            self.kill()