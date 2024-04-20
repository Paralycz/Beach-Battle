from random import choice

def enemy_move(enemy, target):
    random_choice = choice([enemy.use_skill_1, enemy.use_skill_2])
            
    if random_choice == enemy.use_skill_2:
        enemy.skill_2_skill_points -= 1
        if enemy.skill_2_skill_points <= 0:
            random_choice = enemy.use_skill_1
        
    return random_choice(target)