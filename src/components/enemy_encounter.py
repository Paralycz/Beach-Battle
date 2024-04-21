from random import choice

from src.instances.enemies import *

class Encounter:
    
    @staticmethod
    def random_encounter():
        enemy = choice([Ocean_Worm, Sea_Kings_Minion, Rogue_Turtle])
        enemy.reset_hp()
        return enemy