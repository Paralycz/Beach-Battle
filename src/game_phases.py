import pygame, sys


from src.components.game_status import GameStatus
from src.global_state import GlobalState
from src.services.visualization_service import VisualizationServices
from src.instances.player_char import *
from src.components.button import Button
from src.utils.tools import update_background_using_scroll
from src.components.inventory import Inventory
from src.components.attack_action import *
from src.components.enemy_encounter import Encounter


GlobalState.load_main_screen()
VisualizationServices.get_load_main_game_displays()


# Game Phases
def main_menu():
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GlobalState.GAMESTATE = GameStatus.GAME_EXIT
            
    set_up()
    reset()

    VisualizationServices.draw_main_menu(GlobalState.SCREEN)

def combat_phase():
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GlobalState.GAMESTATE = GameStatus.GAME_EXIT
            return
        
    
    # Set up background
    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL, speed=2)
    VisualizationServices.draw_background_with_scroll(GlobalState.SCREEN, VisualizationServices.get_beach_background_image(),GlobalState.SCROLL)
    VisualizationServices.draw_combat_phase(GlobalState.SCREEN)
    

    # Draws Health Bars
    health_bars = GlobalState.create_health_bars()

    for health_bar in health_bars:
        health_bar.draw(GlobalState.SCREEN, health_bar.hp)

    VisualizationServices.draw_health_bar(GlobalState.SCREEN)
    VisualizationServices.draw_health_bar(GlobalState.SCREEN, x=710)


    # Draw Enemy
    VisualizationServices.draw_enemy_sprite(GlobalState.SCREEN)

    # Draw Player
    VisualizationServices.draw_player_sprites(GlobalState.SCREEN)
    
    switch_char(GlobalState.SCREEN)

    check_game_over()

    # Player Actions
    if ActionConfig.game_over == 0:
        switch_char_dead()
        player_skill_1(GlobalState.player)
        player_skill_2(GlobalState.player)
        enemy_attack(GlobalState.enemy)

    elif ActionConfig.game_over == 1:
        GlobalState.SCREEN.blit(VisualizationServices.get_defeat_image(), (0,0))

     # Update Damage Text
    ActionConfig.damage_text_group.update()
    ActionConfig.damage_text_group.draw(GlobalState.SCREEN)

def inventory_phase():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GlobalState.GAMESTATE = GameStatus.GAME_EXIT
            return
    
    VisualizationServices.draw_inventory_phase(GlobalState.SCREEN)
    VisualizationServices.draw_equip_button(GlobalState.SCREEN, x=35, y=295, x_text=90, y_text=312, scale=0.25, character=Drake_Ironfist)
    VisualizationServices.draw_equip_button(GlobalState.SCREEN, x=285, y=295, x_text=340, y_text=312, scale=0.25, character=Hakuro_Yakimura)
    VisualizationServices.draw_equip_button(GlobalState.SCREEN, x=535, y=295, x_text=590, y_text=312, scale=0.25, character=Flamme_Fury)
    VisualizationServices.draw_equip_button(GlobalState.SCREEN, x=785, y=295, x_text=840, y_text=312, scale=0.25, character=Drunk_Uncle)

def game_over_phase():

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GlobalState.GAMESTATE = GameStatus.GAME_EXIT
            return
        
    VisualizationServices.draw_game_over_phase(GlobalState.SCREEN)

def exit_game_phase():
    sys.exit()


# Game Configurations
def reset():
    GlobalState.player = GlobalState.player_inventory[0]

    for character in GlobalState.player_inventory:
        character.reset_hp()
    
def set_up():
    if len(GlobalState.player_inventory) == 0:
        Inventory.add_to_inventory(Drake_Ironfist)
        Inventory.add_to_inventory(Hakuro_Yakimura)
    elif len(GlobalState.player_inventory) == 1:
        Inventory.add_to_inventory(GlobalState.player_inventory[0])
    
    GlobalState.enemy = Encounter.random_encounter()

    ActionConfig.game_over = 0

# Buttons
def switch_char(screen):
    if not hasattr(VisualizationServices, 'switch_button'):
        VisualizationServices.switch_button = Button(950, 550, VisualizationServices.get_char_switch_button_image(), 0.2, VisualizationServices.get_menu_hover_image())
    VisualizationServices.switch_button.draw(screen)

    if VisualizationServices.switch_button.check_input():
        if GlobalState.player == GlobalState.player_inventory[0]:
            GlobalState.player = GlobalState.player_inventory[1]
            if not GlobalState.player_inventory[1].alive:
                GlobalState.player = GlobalState.player_inventory[0]

        elif GlobalState.player == GlobalState.player_inventory[1]:
            GlobalState.player = GlobalState.player_inventory[0]
            if not GlobalState.player_inventory[0].alive:
                GlobalState.player = GlobalState.player_inventory[1]