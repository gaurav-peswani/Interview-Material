from dto.board_component import BoardComponent
from enums.component_type import ComponentType

class Snake(BoardComponent):

    def __init__(self, source: int, destination: int) -> None:
        super().__init__(ComponentType.SNAKE, source, destination)

    def validate(self) -> None:
        if self.destination > self.source:
            print(f"For a Snake, the destination must be lesser than the source.")