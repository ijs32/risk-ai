# My files
from classes.territory_registry import TerritoryRegistry
# Libraries
import json
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

def create_player(name):
    pass

class Player:
    def __init__(self, player_id: int):
        self.player_id = player_id

    def deploy_troops(self, troops: int, registry: TerritoryRegistry):
        raise NotImplementedError

class QAgent(Player):
    def __init__(self, player_id: int):
        super().__init__(player_id) 
        

    def deploy_troops(self, troops: int, registry: TerritoryRegistry):
        raise NotImplementedError
    
    def attack(self, registry: TerritoryRegistry):
        raise NotImplementedError
    
    def simulate_turn(self):
        raise NotImplementedError
    
class LLMAgent(Player):
    def __init__(self, player_id: int, model_name: str):
        super().__init__(player_id)
        
        self.model_name = model_name
        self.instantiate_model()

    def instantiate_model(self):
        self.llm: ChatOllama = ChatOllama(model=self.model_name, format="json", temperature=0)

    def deploy_troops(self, troops: int, registry: TerritoryRegistry):
        json_schema = {
            "deployments": [
                {
                    "territory_id": "id of territory you would like to deploy troops to", 
                    "troop_count": "number of troops you would like to deploy"
                },
            ],
            "required": ["deployments"],
        }

        messages = [
            SystemMessage(f"You are playing classic risk. you are player_{self.player_id} you have {troops} troops to deploy. The current state of the board is as follows: {registry.registry_to_json()}"),
            HumanMessage(
                content="please choose where to deploy troops using the following JSON schema:"
            ),
            HumanMessage(content="{dumps}"),
            HumanMessage(
                content="""
                    Understand that deployments is an array of dictionaries where the key is a territory_id and troop count is 
                    the number you would like to deploy. you must deploy to at least 1 territory. 
                """
            ),
        ]

        prompt = ChatPromptTemplate.from_messages(messages)
        dumps = json.dumps(json_schema, indent=2)

        chain = prompt | self.llm | StrOutputParser()
        llm_selection = json.loads(chain.invoke({"dumps": dumps}))