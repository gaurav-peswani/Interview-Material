from typing import List
from user import User
from agent import Agent
from food_item import FoodItem
from restaurant import Restaurant

class Order:

    def __init__(self, id: str, user: User, restaurant: Restaurant, items: List[FoodItem]) -> None:
        self.id = id
        self.user = user
        self.restaurant = restaurant
        self.items = items

        self.agent = None
        self.status = "PENDING"

    def assign_partner(self, agent: Agent) -> None:
        self.agent = agent
        self.agent.is_available = False