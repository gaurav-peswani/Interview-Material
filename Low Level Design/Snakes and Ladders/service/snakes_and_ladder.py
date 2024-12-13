import time

from player import Player
from board import Board
from dice import Dice
from snake import Snake
from ladder import Ladder

CELLS = 100

class SnakesAndLadders:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.players = {}
            cls._instance.player_order = []
            cls._instance.current_player_index = 0
            cls._instance.finished = False
            cls._instance.winner = None
            cls._instance.board = Board(cell_count=CELLS)
            cls._instance.dice = Dice()
        return cls._instance

    @staticmethod
    def get_instance() -> 'SnakesAndLadders':
        if SnakesAndLadders._instance is None:
            SnakesAndLadders()
        return SnakesAndLadders._instance

    def add_player(self, player: Player) -> None:
        print(f"Player {player.name} added to the game.")
        self.players[player.id] = player

    def add_snake(self, snake: Snake) -> None:
        self.board.place_component(snake)

    def add_ladder(self, ladder: Ladder) -> None:
        self.board.place_component(ladder)

    def roll_dice(self, player: Player) -> int:
        dice_roll = self.dice.roll_dice()
        print(f"Player {player.name} at {player.position} rolled the dice and got a {dice_roll}.")
        return dice_roll

    def move(self, player: Player, step: int) -> None:
        current_position = player.position
        expected_next_position = current_position + step
        actual_next_position = self.board.get_next_position(current_position, step)

        if self.board.is_out_of_board(expected_next_position):
            print(f"Player {player.name} staying at from {actual_next_position}.")
        elif self.board.is_finish(expected_next_position):
            print(f"Player {player.name} has won. Moving from {current_position} to {actual_next_position}.")
            self.finished = True
            self.winner = player
        elif self.board.is_snake(expected_next_position):
            print(f"Player {player.name} has landed on a Snake. Moving from {expected_next_position} to {actual_next_position}.")
        elif self.board.is_ladder(expected_next_position):
            print(f"Player {player.name} has landed on a Ladder. Moving from {expected_next_position} to {actual_next_position}.")
        else:
            print(f"Player {player.name} moving from {current_position} to {actual_next_position}.")

        player.position = self.board.get_next_position(current_position, step)


    def is_finished(self) -> bool:
        return self.finished

    def initialize_players(self) -> None:
        players = sorted(self.players.items())
        self.player_order = players

    def switch_player(self) -> None:
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play_turn(self) -> None:
        current_player = self.player_order[self.current_player_index][1]
        print(f"It is {current_player.name}'s turn.")
        dice_roll = self.roll_dice(current_player)
        self.move(current_player, dice_roll)
        self.switch_player()
        # time.sleep(1)
        print("---------------------------------------------------------")