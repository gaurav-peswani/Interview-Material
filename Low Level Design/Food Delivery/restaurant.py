from food_item import FoodItem

class Restaurant:

    def __init__(self, id: str, name: str, address: int) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.menu = {}

    def add_item(self, food_item: FoodItem) -> None:
        self.menu[food_item.name] = food_item