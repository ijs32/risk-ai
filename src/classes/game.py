# libraries
import random
import pandas as pd
import pprint
from sqlalchemy.sql import text

# my files
from classes.turn import Turn
from classes.territory import Territory
from classes.player import Player
from classes.player import create_player
from mysqlconn.mySQLdb import get_engine
from classes.territory_registry import TerritoryRegistry

TERRITORY_COUNT = 42
PLAYER_COUNT = 3

class Game:
    def __init__(self, player_count=PLAYER_COUNT, territory_count=TERRITORY_COUNT) -> None:
        self.engine = get_engine()
        
        self.player_count = player_count
        self.players: list[Player] = []
        self.create_players()

        self.territory_count = territory_count
        self.territories: list[Territory] = []
        self.create_territories()

        self.initiate_territory_registry()

    def create_players(self):
        for i in range(1, (self.player_count + 1)):
            self.players.append(Player(i))

    def create_territories(self):
        temp_territories = []

        get_territories_sql = text("SELECT * FROM territories")
        with self.engine.connect() as conn:
            result_proxy = conn.execute(get_territories_sql).fetchall()

        territories = list(result_proxy)
        df_territories = pd.DataFrame(territories, columns=["territory_id", "name", "continent_id"])
        for _index, row in df_territories.iterrows():
            get_edges_sql = text("SELECT to_territory_id FROM edges WHERE from_territory_id = :territory_id")
            params = {
                "territory_id": row['territory_id']
            }
            with self.engine.connect() as conn:
                edges = conn.execute(get_edges_sql, params).fetchall()
            
            attrs = {
                "territory_id": row['territory_id'],
                "name": row["name"],
                "continent_id": row["continent_id"],
                "edges": edges
            }
            temp_territories.append(Territory(attrs))
        
        random.shuffle(temp_territories) 
        self.territories = temp_territories

    def initiate_territory_registry(self):

        player_id = 1
        registry: dict[int, list[Territory]] = {}
        for territory in self.territories:

            if player_id not in registry.keys(): registry[player_id] = []
            registry[player_id].append(territory)
            
            if player_id % self.player_count == 0: player_id = 1
            else: player_id += 1

        self.territory_registry = TerritoryRegistry(registry)

    def take_turn(self):
        turn = Turn(self.players, self.territory_registry)

        

