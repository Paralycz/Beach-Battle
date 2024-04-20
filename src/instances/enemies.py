from src.global_state import GlobalState
from src.components.character import Character

GlobalState.load_main_screen()

# Enemies HP, Strength, and Speed are increased by half of the experience of player

Rogue_Turtle = Character(x=830,
                   y=350,
                   type= 'enemy',
                   name='Rogue Turtle',
                   max_hp=170,
                   skill_1_damage=40,
                   skill_2_damage=65,
                   skill_2_skill_points=3)

Sea_Kings_Minion = Character(x=850,
                   y=350,
                   type= 'enemy',
                   name='Sea King\'s Minion',
                   max_hp=190,
                   skill_1_damage=40,
                   skill_2_damage=75,
                   skill_2_skill_points=1)

Ocean_Worm = Character(x=820,
                   y=350,
                   type= 'enemy',
                   name='Ocean Worm',
                   max_hp=250,
                   skill_1_damage=25,
                   skill_2_damage=45,
                   skill_2_skill_points=100)