from classes.territory import Territory

import json

class TerritoryRegistry:
    def __init__(self, registry: dict[int, list[Territory]]) -> None:
        self.registry = registry

    def add(self, player_id, territory):
        self.registry[player_id].append(territory)
    
    def remove(self, player_id, territory):
        self.registry[player_id].remove(territory)

    def get_territories_by_player(self, player_id) -> list[Territory]:
        return self.registry[player_id]
    
    def registry_to_json(self) -> dict:

        registry = {}
        for key, value in self.registry.items():
            registry["player_"+key] = list(map(lambda territory: territory.territory_to_json(), value))
        
        return json.dumps(registry, indent=2)