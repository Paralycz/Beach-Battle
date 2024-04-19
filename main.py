import pygame

from src.game_phases import *
from src.global_state import GlobalState
from src.config import Config

def update_game_displays():
    pygame.display.update()
    pygame.time.Clock().tick(Config.FPS)

def main():
    while True:
        if GlobalState.GAMESTATE == GameStatus.MAIN_MENU:
            main_menu()
        elif GlobalState.GAMESTATE == GameStatus.COMBAT:
            combat_phase()
        elif GlobalState.GAMESTATE == GameStatus.INVENTORY:
            inventory_phase()
        elif GlobalState.GAMESTATE == GameStatus.GAME_OVER:
            game_over_phase()
        elif GlobalState.GAMESTATE == GameStatus.GAME_EXIT:
            exit_game_phase()
        update_game_displays()


if __name__ == '__main__':
    main()