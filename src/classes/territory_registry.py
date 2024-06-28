from classes.territory import Territory

class TerritoryRegistry:
    def __init__(self, registry: dict[int, list[Territory]]) -> None:
        self.territories = registry

    def add(self, player_id, territory):
        self.territories[player_id].append(territory)
    
    def remove(self, player_id, territory):
        self.territories[player_id].remove(territory)

    def get_territories_by_player(self, player_id):
        return self.territories[player_id]