import pygame, os
from pygame.locals import *
from random import randint


from src.services.visualization_service import VisualizationServices
from src.components.attack_action import ActionConfig
from src.components.damage_text import DamageText

class Character:
    def __init__(self, x, y, name, max_hp, skill_1_damage, skill_2_damage, type, skill_2_skill_points=0, 
                 scale=2):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp 
        self.type = type
        self.skill_1_damage = skill_1_damage
        self.skill_2_damage =skill_2_damage
        self.alive = True
        self.calculate = 18
        self.animation_list = [] # Stores the animation list idle skill_1 etc
        self.frame_index = 0
        self.action = 0 # 0: idle, 1: Skill_1, 2: Skill_2, 3: Death 4: Hurt
        self.update_time = pygame.time.get_ticks()
        self.skill_2_skill_points = skill_2_skill_points
        self.skill_2_skill_points_left = self.skill_2_skill_points

        #load idle images 0 
        temp_list = []
        idle_img_path = f'assets/sprites/{self.name}/idle/' 
        num_idle_images = len([name for name in os.listdir(idle_img_path) if os.path.isfile(os.path.join(idle_img_path, name))]) # Gets the amount of images in folder
        for i in range(num_idle_images):
            img  = VisualizationServices.get_sprites_imgs(self.name, 'idle', i)
            img = VisualizationServices.scale(img, scale) # Scale Image
            temp_list.append(img)
        self.animation_list.append(temp_list)


        #load attack1 images 1
        temp_list = []
        attack1_img_path = f'assets/sprites/{self.name}/attack1/' 
        num_attack1_images = len([name for name in os.listdir(attack1_img_path) if os.path.isfile(os.path.join(attack1_img_path, name))]) # Gets the amount of images in folder
        for i in range(num_attack1_images):
            img  = VisualizationServices.get_sprites_imgs(self.name, 'attack1', i)
            img = VisualizationServices.scale(img, scale) # Scale Image
            temp_list.append(img)
        self.animation_list.append(temp_list)


        #load attack2 images 2
        temp_list = []
        attack2_img_path = f'assets/sprites/{self.name}/attack2/' 
        num_attack2_images = len([name for name in os.listdir(attack2_img_path) if os.path.isfile(os.path.join(attack2_img_path, name))]) # Gets the amount of images in folder
        for i in range(num_attack2_images):
            img  = VisualizationServices.get_sprites_imgs(self.name, 'attack2', i)
            img = VisualizationServices.scale(img, scale) # Scale Image
            temp_list.append(img)
        self.animation_list.append(temp_list)


        # load death images 3
        temp_list = []
        death_img_path = f'assets/sprites/{self.name}/death/' 
        num_death_images = len([name for name in os.listdir(death_img_path) if os.path.isfile(os.path.join(death_img_path, name))]) # Gets the amount of images in folder
        for i in range(num_death_images):
            img  = VisualizationServices.get_sprites_imgs(self.name, 'death', i)
            img = VisualizationServices.scale(img, scale) # Scale Image
            temp_list.append(img)
        self.animation_list.append(temp_list)


        # load hurt images 4
        temp_list = []
        hurt_img_path = f'assets/sprites/{self.name}/hurt/' 
        num_hurt_images = len([name for name in os.listdir(hurt_img_path) if os.path.isfile(os.path.join(hurt_img_path, name))]) # Gets the amount of images in folder
        for i in range(num_hurt_images):
            img  = VisualizationServices.get_sprites_imgs(self.name, 'hurt', i)
            img = VisualizationServices.scale(img, scale) # Scale Image
            temp_list.append(img)
        self.animation_list.append(temp_list)
        
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()  # Initialize rect attribute
        self.rect.center = (x, y)

    def update(self):
        animation_cooldown = 120 # Miliseconsd
        # Handle Animation
        # Update Image
        self.image = self.animation_list[self.action][self.frame_index]

        #Check if enough time has passed since the last update
        if pygame.time.get_ticks() - self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        # resets animation if out of frames
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.alive:
                self.sprite_animation() # Resets back to idle
            else:
                if self.action == 3:
                    self.frame_index = len(self.animation_list[self.action]) - 1
                else:
                    self.sprite_animation()

    def sprite_animation(self, action=0):
        self.action = action
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def use_skill_1(self, target):
        percentage = int(self.calculate / 100 * (self.skill_1_damage))
        random_damage = randint(self.skill_1_damage - percentage, self.skill_1_damage)
        target.sprite_animation(4)

        target.hp -= random_damage

        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.sprite_animation(3)

        damage_text = DamageText(target.rect.centerx, target.rect.centery, random_damage, (255, 0, 0))
        ActionConfig.damage_text_group.add(damage_text)

        # Set action to skill 1
        self.action = 1
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    def use_skill_2(self, target):
        percentage = int(self.calculate / 100 * (self.skill_1_damage))
        random_damage = randint(self.skill_2_damage - percentage, self.skill_2_damage)
        self.skill_2_skill_points_left -= 1
        target.sprite_animation(4)
        

        target.hp -= random_damage

        # Check if target is alive
        if target.hp < 1:
            target.hp = 0
            target.alive = False
            target.sprite_animation(3)

        damage_text = DamageText(target.rect.centerx, target.rect.centery, random_damage, (255, 0, 0))
        ActionConfig.damage_text_group.add(damage_text)

        # Set action to skll 2
        self.action = 2
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

    # Configurations
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset_hp(self):
        self.hp = self.max_hp
        self.alive = True
        ActionConfig.action_cooldown = 0
        ActionConfig.current_fighter = 1
        self.skill_2_skill_points_left = self.skill_2_skill_points