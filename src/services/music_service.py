import pygame

from src.components.game_status import GameStatus
from random import choice

pygame.mixer.init()

class MusicService:
    @staticmethod
    def get_combat_musics():
        return ['assets/audio/battle_1.ogg',
                'assets/audio/battle_2.ogg',
                'assets/audio/battle_3.ogg']
    
    @staticmethod
    def play_combat_music():
        if pygame.mixer.music.get_busy():
            return

        playlist = MusicService.get_combat_musics()
        filename = choice(playlist)

        pygame.mixer.music.load(filename)
        pygame.mixer.music.set_volume(0.35)
        pygame.mixer.music.play(1)

    @staticmethod
    def play_main_menu_music():
        if pygame.mixer.music.get_busy():
            return

        pygame.mixer.music.load('assets/audio/menu.ogg')
        pygame.mixer.music.play(-1) # -1 means play in loop
        pygame.mixer.music.set_volume(0.35)

    @staticmethod
    def play_click_sound():
        sound = pygame.mixer.Sound(pygame.mixer.Sound('assets/audio/click.wav'))
        sound.set_volume(0.5)
        sound.play()

    @staticmethod
    def play_skill_1_sound(char_name):
        sound = pygame.mixer.Sound(pygame.mixer.Sound(f'assets/audio/character_sfx/skill_1/{char_name}.wav'))
        sound.set_volume(0.5)
        sound.play()

    @staticmethod
    def play_skill_2_sound(char_name):
        sound = pygame.mixer.Sound(pygame.mixer.Sound(f'assets/audio/character_sfx/skill_2/{char_name}.wav'))
        sound.set_volume(0.5)
        sound.play() 

    @staticmethod
    def play_hurt_sound(char_type):
        sound = pygame.mixer.Sound(pygame.mixer.Sound(f'assets/audio/character_sfx/{char_type}_hurt.wav'))
        sound.set_volume(0.5)
        sound.play()

    @staticmethod
    def play_victory_sound():
        if pygame.mixer.music.get_busy():
            return
            
        pygame.mixer.music.load('assets/audio/victory.ogg')
        pygame.mixer.music.play(1) # -1 means play in loop
        pygame.mixer.music.set_volume(0.35)

    @staticmethod
    def play_defeat_sound():
        if pygame.mixer.music.get_busy():
                return
        
        pygame.mixer.music.load('assets/audio/defeat.ogg')
        pygame.mixer.music.play(1) # -1 means play in loop
        pygame.mixer.music.set_volume(1.5)