from entities.entity import Entity

class Instrument(Entity):

    def __init__(self, id: int, tag: str) -> None:
        super().__init__(id, tag)