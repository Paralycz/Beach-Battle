from pygame import sprite

from src.global_state import GlobalState
from src.components.game_status import GameStatus
from src.services.music_service import MusicService
from src.components.enemy_ai import enemy_move

class ActionConfig:
    current_fighter = 1
    action_wait_time = 90
    action_cooldown = 0
    game_over_cd = 0
    skill_1 = False
    skill_2 = False
    damage_text_group = sprite.Group()


    game_over = 0

def player_skill_1(player):
    if player.alive:
        if ActionConfig.current_fighter == 1:
            ActionConfig.action_cooldown += 1
            if ActionConfig.action_cooldown >= ActionConfig.action_wait_time:
                if ActionConfig.skill_1:
                    player.use_skill_1(GlobalState.enemy)
                    ActionConfig.current_fighter = 2
                    ActionConfig.action_cooldown = 0
                    ActionConfig.skill_1 = False



def player_skill_2(player):
    if player.alive:
        if ActionConfig.current_fighter == 1:
            ActionConfig.action_cooldown += 1
            if ActionConfig.action_cooldown >= ActionConfig.action_wait_time:
                if ActionConfig.skill_2 and player.skill_2_skill_points_left > 0:
                    player.use_skill_2(GlobalState.enemy)
                    ActionConfig.current_fighter = 2
                    ActionConfig.action_cooldown = 0
                    ActionConfig.skill_2 = False


def enemy_attack(enemy):
    if ActionConfig.current_fighter == 2:
        if enemy.alive:

            ActionConfig.action_cooldown += 1
            if ActionConfig.action_cooldown >= ActionConfig.action_wait_time:
                enemy_move(GlobalState.enemy, GlobalState.player)
                ActionConfig.current_fighter = 1
                ActionConfig.action_cooldown = 0

def switch_char_dead():
    if not GlobalState.player.alive:
        ActionConfig.action_cooldown += 1
        if ActionConfig.action_cooldown >= 60:
            # Check if at least one character in the inventory is alive before playing the sound
            if any(character.alive for character in GlobalState.player_inventory):
                MusicService.play_click_sound()
                if GlobalState.player_inventory[0].alive:
                    GlobalState.player = GlobalState.player_inventory[0]
                elif len(GlobalState.player_inventory) > 1 and GlobalState.player_inventory[1].alive:
                    GlobalState.player = GlobalState.player_inventory[1]
                
            ActionConfig.action_cooldown = 0



def check_game_over():
    all_players_dead = all(not char.alive for char in GlobalState.player_inventory)

    if all_players_dead:
        ActionConfig.game_over_cd += 1
        if ActionConfig.game_over_cd >= 90:
            ActionConfig.game_over = -1  # Game over: all players dead
            GlobalState.fade()
            GlobalState.GAMESTATE = GameStatus.GAME_OVER
            ActionConfig.game_over_cd = 0

    elif not GlobalState.enemy.alive:
        ActionConfig.game_over_cd += 1
        if ActionConfig.game_over_cd >= 90:
            ActionConfig.game_over = 1 # Game over: enemy dead
            GlobalState.fade()
            GlobalState.GAMESTATE = GameStatus.GAME_OVER
            ActionConfig.game_over_cd = 0