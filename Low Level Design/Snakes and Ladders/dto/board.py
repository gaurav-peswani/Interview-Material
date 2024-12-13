from dto.cell import Cell
from dto.board_component import BoardComponent
from component_type import ComponentType

class Board:

    def __init__(self, cell_count: int) -> None:
        self._cell_count = cell_count
        self._cells = {}

        self._initialize_board()

    def _initialize_board(self) -> None:
        for index in range(1, self._cell_count + 1):
            self._cells[index] = Cell(index, index)

    def place_component(self, board_component: BoardComponent) -> None:
        self._cells[board_component.source] = board_component

    def is_snake(self, cell: int) -> bool:
        return self._cells[cell].type == ComponentType.SNAKE

    def is_ladder(self, cell: int) -> bool:
        return self._cells[cell].type == ComponentType.LADDER

    def is_finish(self, cell: int) -> bool:
        return cell == self._cell_count

    def is_out_of_board(self, cell) -> bool:
        return cell > self._cell_count

    def get_next_position(self, position: int, step: int) -> int:
        cell = position + step
        if self.is_out_of_board(cell):
            return position
        return self._cells[cell].destination