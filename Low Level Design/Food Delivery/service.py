from typing import List
from uuid import uuid4
from restaurant import Restaurant
from food_item import FoodItem
from agent import Agent
from order import Order
from order_status import OrderStatus
from user import User


class Service:

    _instance = None

    def __new__(cls) -> None:
        if cls._instance is None:
            cls._instance = super().__new__()
            cls._instance.users = {}
            cls._instance.restaurants = {}
            cls._instance.agents = {}
            cls._instance.orders = {}
        return cls._instance
    
    @staticmethod
    def get_instance() -> Service:
        if Service._instance is None:
            Service()
        return Service._instance
    
    # Registation
    def add_restaurant(self, restaurant: Restaurant) -> None:
        self.restaurants[id] = restaurant

    def add_user(self, user: User) -> None:
        self.users[user.id] = user

    def add_agent(self, agent: Agent) -> None:
        self.agents[agent.id] = agent

    def add_food_item(self, restaurant_id: str, food_item: FoodItem) -> None:
        self.restaurants[restaurant_id].add_item(food_item)

    # Order placement
    def list_restaurants(self) -> List[Restaurant]:
        return self.restaurants.values()
    
    def place_order(self, user: User, restaurant: Restaurant, food_items: List[FoodItem]) -> Order:
        order_id = str(uuid4())
        order = Order(
            id=order_id,
            user=user,
            restaurant=restaurant,
            items=food_items
        )
        order.status = OrderStatus.CONFIRMED
        self.orders[order_id] = order
        return order                                            
    
    # delivery partner assignment
    def assign_partner(self, order: Order) -> None:
        for partner in self.agents:
            if partner.is_available:
                order.assign_partner(agent=partner)

    # 