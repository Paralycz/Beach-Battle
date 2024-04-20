from src.components.character import Character
from src.global_state import GlobalState

GlobalState.load_main_screen()

Drake_Ironfist = Character(x=240,
                   y=330,
                   type='player',
                   name='Drake Ironfist',
                   max_hp=110,
                   skill_1_damage=25,
                   skill_2_damage=35,
                   skill_2_skill_points=2,
                   scale=1.3)

Hakuro_Yakimura = Character(x=230,
                   y=330,
                   type='player',
                   name='Hakuro Yakimura',
                   max_hp= 80,
                   skill_1_damage=25,
                   skill_2_damage=60,
                   skill_2_skill_points=1,
                   scale=1.3)

Flamme_Fury = Character(x=275,
                   y=302,
                   type='player',
                   name='Flamme Fury',
                   max_hp=100,
                   skill_1_damage=28,
                   skill_2_damage=50,
                   skill_2_skill_points=1,
                   scale=1.5)

Drunk_Uncle = Character(x=240,
                   y=300,
                   type='player',
                   name='Drunk Uncle',
                   max_hp=130,
                   skill_1_damage=20,
                   skill_2_damage=40,
                   skill_2_skill_points=1,
                   scale=1.55)
