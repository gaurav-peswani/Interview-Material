from dto.board_component import BoardComponent
from enums.component_type import ComponentType

class Ladder(BoardComponent):

    def __init__(self, source: int, destination: int) -> None:
        super().__init__(ComponentType.LADDER, source, destination)

    def validate(self) -> None:
        if self.destination < self.source:
            print(f"For a Ladder, the destination must be greater than the source.")