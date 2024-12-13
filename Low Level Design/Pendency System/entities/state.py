from entities.entity import Entity

class State(Entity):

    def __init__(self, id: int, name: str) -> None:
        super().__init__(id, name)