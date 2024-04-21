import pygame


from src.components.game_status import GameStatus
from src.config import Config
from src.components.health_bar import HealthBar


class GlobalState:
    GAMESTATE = GameStatus.MAIN_MENU
    SCREEN = None
    SCROLL = 0
    player_inventory = []
    enemy = None # Sets up sprites
    player = None


    @staticmethod
    def load_main_screen():
        pygame.init()
        WINDOW = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
        WINDOW.fill('black')
        GlobalState.SCREEN = WINDOW

    def fade(width=Config.WIDTH, height=Config.HEIGHT, fade_music=True):
        fade = pygame.Surface((width, height))
        fade.fill((0, 0, 0))
        for alpha in range(0, 256):  # Adjusted alpha range
            fade.set_alpha(alpha)
            GlobalState.SCREEN
            GlobalState.SCREEN.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)
        
        if fade_music:
            pygame.mixer.music.fadeout(1400)

    @staticmethod
    def create_health_bars():
        player_health_bar = HealthBar(x=133, y=210, hp=GlobalState.player.hp, max_hp=GlobalState.player.max_hp)
        enemy_health_bar = HealthBar(x=762, y=210, hp=GlobalState.enemy.hp, max_hp=GlobalState.enemy.max_hp)
        return [player_health_bar, enemy_health_bar]