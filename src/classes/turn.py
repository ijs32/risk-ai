from classes.player import Player
from classes.territory_registry import TerritoryRegistry
from math import floor

class Turn:
    def __init__(self, players: list[Player], territory_registry: TerritoryRegistry) -> None:
        self.players = players
        self.territory_registry = territory_registry

        for player in self.players:
            self.award_troops(player)
            self.attack(player)
        pass

    def award_troops(self, player: Player):
        
        troops_awarded = 3 # min awarded

        territories = self.territory_registry.get_territories_by_player(player.player_id)
        territory_count = len(territories)

        troops_from_territories = 0
        if territory_count > 9: 
            territory_count = territory_count - 9
            troops_from_territories = floor(territory_count / 3)

        troops_awarded += troops_from_territories

        player.deploy_troops(troops_awarded, self.territory_registry)


    def attack(self, player: Player):
        raise NotImplementedError