from enum import Enum

class GameStatus(Enum):
    MAIN_MENU = 0
    COMBAT = 1
    INVENTORY = 2
    GAME_OVER = 3
    GAME_EXIT = 4