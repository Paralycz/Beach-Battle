from src.global_state import GlobalState


class Inventory:
    max_capacity = 2

    def check_player_inventory(character):
        if character in GlobalState.player_inventory:
            return True
        else:
            return False

    def add_to_inventory(player):
        if len(GlobalState.player_inventory) < Inventory.max_capacity:
            GlobalState.player_inventory.append(player)

        elif len(GlobalState.player_inventory) >= Inventory.max_capacity:
            GlobalState.player_inventory.pop(0)
            GlobalState.player_inventory.append(player)

    
    def remove_from_inventory(player):
        GlobalState.player_inventory.remove(player)
        Inventory.equipped = False


    def check_inventory():
        return f'Slots Available: {len(GlobalState.player_inventory)}/{Inventory.max_capacity}'