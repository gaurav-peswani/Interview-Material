from snakes_and_ladder import SnakesAndLadders
from player import Player
from snake import Snake
from ladder import Ladder

class Demo:

    @staticmethod
    def run() -> None:
        game = SnakesAndLadders.get_instance()

        player1 = Player(id=1, name="A")
        player2 = Player(id=2, name="B")
        player3 = Player(id=3, name="C")
        player4 = Player(id=4, name="D")

        snake1 = Snake(32, 5)
        snake2 = Snake(15, 2)
        snake3 = Snake(99, 1)
        snake4 = Snake(64, 10)

        ladder1 = Ladder(2, 11)
        ladder2 = Ladder(60, 71)
        ladder3 = Ladder(53, 65)
        ladder4 = Ladder(78, 89)

        game.add_snake(snake1)
        game.add_snake(snake2)
        game.add_snake(snake3)
        game.add_snake(snake4)

        game.add_ladder(ladder1)
        game.add_ladder(ladder2)
        game.add_ladder(ladder3)
        game.add_ladder(ladder4)

        game.add_player(player1)
        game.add_player(player2)
        game.add_player(player3)
        game.add_player(player4)

        game.initialize_players()

        print("\nStarting Game...\n")

        while not game.is_finished():
            game.play_turn()

        print(f"Winner: {game.winner.name}!")

if __name__ == "__main__":
    Demo.run()
