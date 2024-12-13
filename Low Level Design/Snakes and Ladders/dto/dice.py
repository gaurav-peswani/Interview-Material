from random import randint

class Dice:

    def __init__(self) -> None:
        pass

    def roll_dice(self) -> int:
        return randint(1, 6)