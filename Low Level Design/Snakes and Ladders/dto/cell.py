from dto.board_component import BoardComponent
from enums.component_type import ComponentType

class Cell(BoardComponent):

    def __init__(self, source: int, destination: int) -> None:
        super().__init__(ComponentType.CELL, source, destination)

    def validate(self) -> None:
        pass