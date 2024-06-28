from classes.territory import Territory
from classes.territory_registry import TerritoryRegistry
def create_player(name):
    pass

class Player:
    def __init__(self, name):
        self.name = name

    def deploy_troops(self, troops: int, registry: TerritoryRegistry):
        raise NotImplementedError

class QAgent(Player):
    def __init__(self, name):
        super().__init__(name)
    
    def simulate_turn(self):
        raise NotImplementedError