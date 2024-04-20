from random import choice

def enemy_move(enemy, target):
    random_choice = choice([enemy.use_skill_1, enemy.use_skill_2])
            
    if random_choice == enemy.use_skill_2:
        if enemy.skill_2_skill_points_left <= 0:
            random_choice = enemy.use_skill_1
        
    return random_choice(target)
