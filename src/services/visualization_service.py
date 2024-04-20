import pygame

from src.components.button import *
from src.components.game_status import GameStatus
from src.global_state import GlobalState
from src.utils.tools import sine, update_background_using_scroll
from src.services.music_service import MusicService
from src.components.attack_action import ActionConfig
from src.components.inventory import Inventory


class VisualizationServices:

    @staticmethod
    def get_sprites_imgs(name, action :str, index):
        return pygame.image.load(f'assets/sprites/{name}/{action}/{index}.png').convert_alpha()
    
    @staticmethod
    def scale(img, scale):
        return pygame.transform.scale(img, (img.get_width() * scale, img.get_height() * scale))
    
    @staticmethod
    def get_font(size=5):
        return pygame.font.Font('assets/font/DePixelSchmal.ttf', size)

    @staticmethod
    def get_menu_hover_image():
        return pygame.image.load('assets/buttons/hover/menu_hover.png').convert_alpha()
    
    @staticmethod
    def get_inventory_bg_image():
        return pygame.image.load('assets/background/inventory_bg.png').convert_alpha()
    
    @staticmethod
    def get_hakuro_icon_image():
        return pygame.image.load('assets/icons/hakuro_icon.png').convert_alpha()
    
    @staticmethod
    def get_uncle_icon_image():
        return pygame.image.load('assets/icons/uncle_icon.png').convert_alpha()
    
    @staticmethod
    def get_drake_icon_image():
        return pygame.image.load('assets/icons/drake_icon.png').convert_alpha()
    
    @staticmethod
    def get_victory_image():
        return pygame.image.load('assets/icons/victory.png').convert_alpha()
    
    @staticmethod
    def get_defeat_image():
        return pygame.image.load('assets/icons/defeat.png').convert_alpha()
    
    @staticmethod
    def get_flamme_icon_image():
        return pygame.image.load('assets/icons/flamme_icon.png').convert_alpha()
    
    @staticmethod
    def get_health_bar_img():
        return pygame.image.load('assets/icons/health_bar.png').convert_alpha()
    
    @staticmethod
    def get_panel_img():
        return pygame.image.load('assets/background/panel2.png').convert_alpha()

    @staticmethod
    def get_play_button_image():
        return pygame.image.load('assets/buttons/play_button.png').convert_alpha()
    
    @staticmethod
    def get_run_button_image():
        return pygame.image.load('assets/buttons/run_button.png').convert_alpha()
    
    
    @staticmethod
    def get_game_title_image():
        return pygame.image.load('assets/icons/game_title.png').convert_alpha()

    @staticmethod
    def get_menu_background_image():
        return pygame.image.load('assets/background/menu_bg.png').convert_alpha()
    
    @staticmethod
    def get_char_shadows_img():
        return pygame.image.load('assets/background/char_shadows.png').convert_alpha()

    @staticmethod
    def get_load_main_game_displays():
        pygame.display.set_caption('Beach Battle')
        pygame.display.set_icon(VisualizationServices.get_game_title_image())
    
    @staticmethod
    def get_beach_background_image():
        return pygame.image.load('assets/background/beach_bg.png').convert_alpha()
    
    @staticmethod
    def get_inventory_panel_image():
        return pygame.image.load('assets/background/inventory_panel2.png').convert_alpha()
    
    @staticmethod
    def get_quit_button_image():
        return pygame.image.load('assets/buttons/exit.png').convert_alpha()
    
    @staticmethod
    def get_home_button_image():
        return pygame.image.load('assets/buttons/home_button.png').convert_alpha()
    
    def get_home_hover_image():
        return pygame.image.load('assets/buttons/hover/home_hover.png').convert_alpha()
    
    @staticmethod
    def get_skill_1_button_image():
        return pygame.image.load('assets/buttons/skill_1_button.png').convert_alpha()
    
    @staticmethod
    def get_skill_2_button_image():
        return pygame.image.load('assets/buttons/skill_2_button.png').convert_alpha()
    
    @staticmethod
    def get_equip_button_image():
        return pygame.image.load('assets/buttons/equip_button.png').convert_alpha()
    
    def get_equip_hover_image():
        return pygame.image.load('assets/buttons/hover/equip_hover.png').convert_alpha()
    
    def get_exit_hover_image():
        return pygame.image.load('assets/buttons/hover/exit_hover.png').convert_alpha()
    
    @staticmethod
    def get_char_switch_button_image():
        return pygame.image.load('assets/buttons/switch_char_button.png').convert_alpha()
    
    @staticmethod
    def get_inventory_button_image():
        return pygame.image.load('assets/buttons/inventory_button.png').convert_alpha()
    
    # Draw Text
    @staticmethod
    def draw_text(screen, text, font, color, x, y):
        img = font.render(text, True, color)
        screen.blit(img, (x, y))

    # Draw Health Bar
    @staticmethod
    def draw_health_bar(screen, x=80, y=160):
        img = VisualizationServices.get_health_bar_img()
        img = VisualizationServices.scale(img, 0.5)
        screen.blit(img, (x, y))

    # Draw Others

    @staticmethod
    def draw_game_over(screen):
        y = sine(200.0, 1280, 10.0, 0)
        victory = VisualizationServices.get_victory_image()
        defeat = VisualizationServices.get_defeat_image()

        if ActionConfig.game_over == 1:
            screen.blit(victory, (0,y))
            MusicService.play_victory_sound()

        elif ActionConfig.game_over == -1:
            screen.blit(defeat, (0,y))
            MusicService.play_defeat_sound()
        
    @staticmethod
    def draw_player_icons(screen):
        hakaru_icon = VisualizationServices.get_hakuro_icon_image()
        drake_icon = VisualizationServices.get_drake_icon_image()
        flamme_icon = VisualizationServices.get_flamme_icon_image()
        drunk_uncle = VisualizationServices.get_uncle_icon_image()

        screen.blit(VisualizationServices.scale(drake_icon, 0.3), (60, 150))
        screen.blit(VisualizationServices.scale(hakaru_icon, 0.3), (310, 150))
        screen.blit(VisualizationServices.scale(flamme_icon, 0.3), (560, 150))
        screen.blit(VisualizationServices.scale(drunk_uncle, 0.3), (810, 150))

    def draw_inventory_panel(screen):
        panel = VisualizationServices.get_inventory_panel_image()
        screen.blit(panel, (0,0))
    
    @staticmethod
    def draw_panel(screen):
        panel = VisualizationServices.get_panel_img()
        screen.blit(panel, (0,30))

    @staticmethod
    def draw_char_shadows(screen):
        char_shadows = VisualizationServices.get_char_shadows_img()
        screen.blit(char_shadows, (100,465))

    @staticmethod
    def draw_game_title(screen):
        y = sine(200.0, 1280, 10.0, -30)
        title = VisualizationServices.get_game_title_image()
        title = VisualizationServices.scale(title, 0.75)
        screen.blit(title, (370, y))


    # Draw Buttons

    @staticmethod
    def draw_equip_button(screen, x, y, x_text, y_text, scale, character):
        button_name = f'{character.name}_equip_button'

        if not hasattr(VisualizationServices, button_name):
            setattr(VisualizationServices, button_name, Button(x, y, VisualizationServices.get_equip_button_image(), scale, hovering_img=VisualizationServices.get_equip_hover_image()))

        button_instance = getattr(VisualizationServices, button_name)
        button_instance.draw(screen)

        if Inventory.check_player_inventory(character):
            VisualizationServices.draw_text(screen, 'Unequip', VisualizationServices.get_font(25), 'red', x_text-10, y_text)
        else:
            VisualizationServices.draw_text(screen, 'Equip', VisualizationServices.get_font(25), (76, 153, 0), x_text, y_text)

        if button_instance.check_input():
            MusicService.play_click_sound()
            if character in GlobalState.player_inventory:
                Inventory.remove_from_inventory(character)
            else:
                Inventory.add_to_inventory(character)



    @staticmethod
    def draw_exit_button(screen, state, x=1020, y=570, scale=0.15):
        quit_button = Button(x, y, VisualizationServices.get_quit_button_image(), scale, VisualizationServices.get_exit_hover_image())
        quit_button.draw(screen)

        if quit_button.check_input():
            MusicService.play_click_sound()

            GlobalState.fade(fade_music=False)
            GlobalState.GAMESTATE = state  

    @staticmethod
    def draw_play_button(screen):
        MusicService.play_main_menu_music()

        y = sine(200.0, 1280, 10.0, 390)
        VisualizationServices.play_button = Button(590, y, VisualizationServices.get_play_button_image(), 0.8, hovering_img=VisualizationServices.get_menu_hover_image())

        VisualizationServices.play_button.draw(screen)

        if VisualizationServices.play_button.check_input():
            MusicService.play_click_sound()
            MusicService.play_main_menu_music()
            GlobalState.fade()
            GlobalState.GAMESTATE = GameStatus.COMBAT

    def draw_inventory_button(screen):
        y = sine(200.0, 1280, 10.0, 390)
        VisualizationServices.inventory_button = Button(410, y, VisualizationServices.get_inventory_button_image(), 0.8, hovering_img=VisualizationServices.get_menu_hover_image())

        VisualizationServices.inventory_button.draw(screen)

        if VisualizationServices.inventory_button.check_input():
            MusicService.play_click_sound()
            GlobalState.fade(fade_music=False)
            GlobalState.GAMESTATE = GameStatus.INVENTORY

    def draw_home_button(screen):
        y = sine(200.0, 1280, 10.0, 290)
        VisualizationServices.play_button = Button(450, y, VisualizationServices.get_home_button_image(), 1.3, hovering_img=VisualizationServices.get_home_hover_image())

        VisualizationServices.play_button.draw(screen)

        if VisualizationServices.play_button.check_input():
            MusicService.play_click_sound()
            GlobalState.fade(fade_music=True)
            GlobalState.GAMESTATE = GameStatus.MAIN_MENU

    @staticmethod
    def draw_run_button(screen):
        MusicService.play_combat_music()
        run_button = Button(490, 540, VisualizationServices.get_run_button_image(), 0.23, hovering_img=VisualizationServices.get_menu_hover_image())

        run_button.draw(screen)
        if run_button.check_input():
            MusicService.play_click_sound()
            GlobalState.fade()
            GlobalState.GAMESTATE = GameStatus.MAIN_MENU

    @staticmethod
    def draw_skill_1_button(screen):
        if not hasattr(VisualizationServices, 'skill_1_button'): # Creates instance of button outside this method
            VisualizationServices.skill_1_button = Button(120, 565, VisualizationServices.get_skill_1_button_image(), 0.16, hovering_img=VisualizationServices.get_menu_hover_image())

        VisualizationServices.skill_1_button.draw(screen)

        if VisualizationServices.skill_1_button.check_input():
            MusicService.play_click_sound()
            ActionConfig.skill_1 = True

                
    
    @staticmethod
    def draw_skill_2_button(screen, player):
        if not hasattr(VisualizationServices, 'skill_2_button'): # Creates instance of button outside this method
            VisualizationServices.skill_2_button = Button(30, 565, VisualizationServices.get_skill_2_button_image(), 0.16, hovering_img=VisualizationServices.get_menu_hover_image())

        VisualizationServices.skill_2_button.draw(screen)
        VisualizationServices.draw_text(screen, f"{player.skill_2_skill_points_left}/{player.skill_2_skill_points}", VisualizationServices.get_font(18), 'red', 55, 545)

        if VisualizationServices.skill_2_button.check_input():
            MusicService.play_click_sound()
            ActionConfig.skill_2 = True

    # Draw Backgrounds

    @staticmethod
    def draw_background_with_scroll(screen, background_img, scroll=0):
        background = background_img
        background_width = background.get_width()

        # Calculate the position for drawing the background based on the scroll
        draw_pos_x = scroll % background_width

        # Draw two copies of the background to create the illusion of seamless scrolling
        screen.blit(background, (draw_pos_x, 0))
        screen.blit(background, (draw_pos_x - background_width, 0))
    
    # Draw Sprites
    
    @staticmethod
    def draw_player_sprites(screen):
        VisualizationServices.draw_text(screen, GlobalState.player.name, VisualizationServices.get_font(20), 'white', 140, 185) # Player Name
        VisualizationServices.draw_text(screen, f"HP: {GlobalState.player.hp}/{GlobalState.player.max_hp}", VisualizationServices.get_font(11), 'white', 140, 225)
        GlobalState.player.update()
        GlobalState.player.draw(screen)

    def draw_enemy_sprite(screen):
        VisualizationServices.draw_text(screen, GlobalState.enemy.name, VisualizationServices.get_font(20), 'white', 775, 185) 
        VisualizationServices.draw_text(screen, f"HP: {GlobalState.enemy.hp}/{GlobalState.enemy.max_hp}", VisualizationServices.get_font(11), 'white', 775, 225) # Player HP first and then Enemy
        GlobalState.enemy.update()
        GlobalState.enemy.draw(screen)
    
    # Game Phases
    @staticmethod
    def draw_main_menu(screen):
        # Set up background
        background = VisualizationServices.get_menu_background_image()
        GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL, speed=1)
        VisualizationServices.draw_background_with_scroll(GlobalState.SCREEN, background, GlobalState.SCROLL)
        
        # Set up buttons and title
        VisualizationServices.draw_game_title(screen)
        VisualizationServices.draw_play_button(screen)
        VisualizationServices.draw_inventory_button(screen)
        VisualizationServices.draw_exit_button(screen, GameStatus.GAME_EXIT)

    @staticmethod
    def draw_combat_phase(screen):
        VisualizationServices.draw_panel(screen)
        VisualizationServices.draw_char_shadows(screen)
        VisualizationServices.draw_run_button(screen)
        VisualizationServices.draw_skill_1_button(screen)
        VisualizationServices.draw_skill_2_button(screen, GlobalState.player)

    def draw_inventory_phase(screen):
        # Background
        background = VisualizationServices.get_inventory_bg_image()
        GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL, speed=1)
        VisualizationServices.draw_background_with_scroll(GlobalState.SCREEN, background, GlobalState.SCROLL)

        # Inventory
        VisualizationServices.draw_inventory_panel(screen)
        VisualizationServices.draw_player_icons(screen)
        VisualizationServices.draw_exit_button(screen, GameStatus.MAIN_MENU, x=930, y=50, scale =0.2)
        VisualizationServices.draw_text(screen, Inventory.check_inventory(), VisualizationServices.get_font(25), 'white', 40, 580)

    def draw_game_over_phase(screen):
        background = VisualizationServices.get_inventory_bg_image()
        GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL, speed=1)
        VisualizationServices.draw_background_with_scroll(GlobalState.SCREEN, background, GlobalState.SCROLL)

        VisualizationServices.draw_game_over(screen)
        VisualizationServices.draw_home_button(screen)