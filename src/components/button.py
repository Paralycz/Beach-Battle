import pygame

from src.global_state import GlobalState

GlobalState.load_main_screen()

class Button:
    def __init__(self, x, y, image, scale, hovering_img):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()  # Creates rectangle for the button
        self.rect.topleft = (x, y)
        self.hovering_img = pygame.transform.scale(hovering_img, (int(width * scale), int(height * scale))) if hovering_img else None
        self.clicked = False

    def draw(self, surface):
        pos = pygame.mouse.get_pos()
        
        # Draw button
        if self.rect.collidepoint(pos):
            if self.hovering_img:
                surface.blit(self.hovering_img, self.rect.topleft)
            else:
                surface.blit(self.image, self.rect.topleft)
        else:
            surface.blit(self.image, self.rect.topleft)  # Draws buttons in surface

    def check_input(self):
        action = False
        pos = pygame.mouse.get_pos()

        # Check for click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:  # If left mouse button is pressed and the button was not clicked before
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            
        return action