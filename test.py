# Libraries
import json
from langchain_community.chat_models import ChatOllama
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

llm: ChatOllama = ChatOllama(model="llama3", format="json", temperature=0)

board_state = {
  "player_1": [
    {
      "territory_id": 18,
      "name": "Congo",
      "continent_id": 3,
      "edges": [
        16,
        20,
        19
      ]
    },
    {
      "territory_id": 39,
      "name": "Peru",
      "continent_id": 6,
      "edges": [
        38,
        40,
        41
      ]
    },
    {
      "territory_id": 4,
      "name": "Eastern Australia",
      "continent_id": 1,
      "edges": [
        2,
        3
      ]
    },
    {
      "territory_id": 32,
      "name": "Alberta",
      "continent_id": 5,
      "edges": [
        33,
        30,
        29,
        35
      ]
    },
    {
      "territory_id": 21,
      "name": "Madagascar",
      "continent_id": 3,
      "edges": [
        19,
        20
      ]
    },
    {
      "territory_id": 12,
      "name": "Siberia",
      "continent_id": 2,
      "edges": [
        8,
        10,
        42,
        14,
        5
      ]
    },
    {
      "territory_id": 6,
      "name": "India",
      "continent_id": 2,
      "edges": [
        15,
        7,
        5,
        13
      ]
    },
    {
      "territory_id": 35,
      "name": "Western United States",
      "continent_id": 5,
      "edges": [
        37,
        36,
        33,
        32
      ]
    },
    {
      "territory_id": 27,
      "name": "Northern Europe",
      "continent_id": 4,
      "edges": [
        28,
        25,
        26,
        24,
        23
      ]
    },
    {
      "territory_id": 42,
      "name": "Yakutsk",
      "continent_id": 2,
      "edges": [
        10,
        11,
        12
      ]
    },
    {
      "territory_id": 15,
      "name": "Middle East",
      "continent_id": 2,
      "edges": [
        6,
        13,
        24,
        17,
        20,
        28
      ]
    },
    {
      "territory_id": 13,
      "name": "Afghanistan",
      "continent_id": 2,
      "edges": [
        6,
        14,
        15,
        24,
        5
      ]
    },
    {
      "territory_id": 5,
      "name": "China",
      "continent_id": 2,
      "edges": [
        7,
        6,
        13,
        14,
        12,
        8
      ]
    },
    {
      "territory_id": 17,
      "name": "Egypt",
      "continent_id": 3,
      "edges": [
        15,
        20,
        16,
        28
      ]
    }
  ],
  "player_2": [
    {
      "territory_id": 14,
      "name": "Ural",
      "continent_id": 2,
      "edges": [
        13,
        12,
        24,
        5
      ]
    },
    {
      "territory_id": 37,
      "name": "Central America",
      "continent_id": 5,
      "edges": [
        38,
        35,
        36
      ]
    },
    {
      "territory_id": 40,
      "name": "Brazil",
      "continent_id": 6,
      "edges": [
        38,
        39,
        41,
        16
      ]
    },
    {
      "territory_id": 41,
      "name": "Argentina",
      "continent_id": 6,
      "edges": [
        39,
        40
      ]
    },
    {
      "territory_id": 16,
      "name": "North Africa",
      "continent_id": 3,
      "edges": [
        28,
        25,
        40,
        17,
        20,
        18
      ]
    },
    {
      "territory_id": 23,
      "name": "Scandinavia",
      "continent_id": 4,
      "edges": [
        27,
        24,
        26,
        22
      ]
    },
    {
      "territory_id": 34,
      "name": "Quebec",
      "continent_id": 5,
      "edges": [
        36,
        33,
        31
      ]
    },
    {
      "territory_id": 36,
      "name": "Eastern United States",
      "continent_id": 5,
      "edges": [
        37,
        35,
        33,
        34
      ]
    },
    {
      "territory_id": 28,
      "name": "Southern Europe",
      "continent_id": 4,
      "edges": [
        15,
        16,
        17,
        25,
        27,
        24
      ]
    },
    {
      "territory_id": 2,
      "name": "New Guinea",
      "continent_id": 1,
      "edges": [
        1,
        3,
        4
      ]
    },
    {
      "territory_id": 10,
      "name": "Irkutsk",
      "continent_id": 2,
      "edges": [
        8,
        11,
        12,
        42
      ]
    },
    {
      "territory_id": 7,
      "name": "Siam",
      "continent_id": 2,
      "edges": [
        5,
        6,
        1
      ]
    },
    {
      "territory_id": 38,
      "name": "Venezuela",
      "continent_id": 6,
      "edges": [
        39,
        40,
        37
      ]
    },
    {
      "territory_id": 19,
      "name": "South Africa",
      "continent_id": 3,
      "edges": [
        18,
        20,
        21
      ]
    }
  ],
  "player_3": [
    {
      "territory_id": 30,
      "name": "Northwest Territory",
      "continent_id": 5,
      "edges": [
        32,
        29,
        31,
        33
      ]
    },
    {
      "territory_id": 9,
      "name": "Japan",
      "continent_id": 2,
      "edges": [
        8,
        11
      ]
    },
    {
      "territory_id": 20,
      "name": "East Africa",
      "continent_id": 3,
      "edges": [
        16,
        17,
        18,
        19,
        21,
        15
      ]
    },
    {
      "territory_id": 3,
      "name": "Western Australia",
      "continent_id": 1,
      "edges": [
        1,
        2,
        4
      ]
    },
    {
      "territory_id": 26,
      "name": "Great Britain",
      "continent_id": 4,
      "edges": [
        25,
        27,
        23,
        22
      ]
    },
    {
      "territory_id": 8,
      "name": "Mongolia",
      "continent_id": 2,
      "edges": [
        5,
        9,
        10,
        11,
        12
      ]
    },
    {
      "territory_id": 11,
      "name": "Kamchatka",
      "continent_id": 2,
      "edges": [
        8,
        9,
        10,
        42,
        29
      ]
    },
    {
      "territory_id": 24,
      "name": "Ukraine",
      "continent_id": 4,
      "edges": [
        13,
        14,
        15,
        28,
        27,
        23
      ]
    },
    {
      "territory_id": 29,
      "name": "Alaska",
      "continent_id": 5,
      "edges": [
        11,
        30,
        32
      ]
    },
    {
      "territory_id": 33,
      "name": "Ontario",
      "continent_id": 5,
      "edges": [
        35,
        36,
        34,
        32,
        30,
        31
      ]
    },
    {
      "territory_id": 31,
      "name": "Greenland",
      "continent_id": 5,
      "edges": [
        22,
        30,
        33,
        34
      ]
    },
    {
      "territory_id": 25,
      "name": "Western Europe",
      "continent_id": 4,
      "edges": [
        16,
        28,
        27,
        26
      ]
    },
    {
      "territory_id": 1,
      "name": "Indonesia",
      "continent_id": 1,
      "edges": [
        2,
        3,
        7
      ]
    },
    {
      "territory_id": 22,
      "name": "Iceland",
      "continent_id": 4,
      "edges": [
        23,
        26,
        31
      ]
    }
  ]
}
board_state = json.dumps(board_state, indent=2)

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
    SystemMessage(f"You are playing classic risk. you are player_1 you have 5 troops to deploy. The current state of the board is as follows: {board_state}"),
    HumanMessage(
        content="please choose where to deploy troops using the following JSON schema:"
    ),
    HumanMessage(content="{dumps}"),
    HumanMessage(
        content="""
            Understand that deployments is an array of dictionaries where the key is a territory_id and troop count is 
            the number you would like to deploy. you must deploy to at least 1 territory. 
            You can only deploy to territories within the player_1 territory array provided to you with the state of the board
        """
    ),
]

prompt = ChatPromptTemplate.from_messages(messages)
dumps = json.dumps(json_schema, indent=2)

chain = prompt | llm | StrOutputParser()
print(chain.invoke({"dumps": dumps}))