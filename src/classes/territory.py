class Territory:
    def __init__(self, attrs: list) -> None:

        self._player = None
        self._territory_id = attrs["territory_id"]
        self._name = attrs["name"]
        self._continent_id = attrs["continent_id"]
        self._edges = attrs["edges"]

    @property
    def player(self) -> int:
        return self._player

    @player.setter
    def player(self, value: int):
        self._player = value

    @property
    def territory_id(self) -> int:
        return self._territory_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def continent_id(self) -> int:
        return self._continent_id

    @property
    def edges(self) -> list:
        return self._edges