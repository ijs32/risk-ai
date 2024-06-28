from classes.player import Player
from classes.territory_registry import TerritoryRegistry

class Turn:
    def __init__(self, players: list[Player], territory_registry: TerritoryRegistry) -> None:
        self.players = players
        self.territory_registry = territory_registry

        for player in self.players:
            self.award_troops(player)
        pass

    def award_troops(self, player: Player):
        
        troops_awarded = 0
        player.deploy_troops(troops_awarded, self.territory_registry)

        pass