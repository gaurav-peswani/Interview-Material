from entities.entity import Entity

class City(Entity):

    def __init__(self, id: int, tag: str) -> None:
        super().__init__(id, tag)