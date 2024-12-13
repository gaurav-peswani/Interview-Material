import time

from enums.auction_status import AuctionStatus
from entities.bid import Bid

class Auction:

    def __init__(self, id: str, item: str, description: str, starting_price: int, duration: int, owner_id: str) -> None:
        self._id = id
        self._item = item
        self._description = description
        self._starting_price = starting_price
        self._duration = duration
        self._owner_id = owner_id

        self._status = AuctionStatus.INITIALIZED
        self._current_price = starting_price
        self._current_winner = None
        self._end_time = None

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._status = value

    @property
    def starting_price(self):
        return self._starting_price

    @property
    def duration(self):
        return self._duration

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def item(self):
        return self._item

    @property
    def owner_id(self):
        return self._owner_id

    @property
    def current_price(self):
        return self._current_price

    @property
    def current_winner(self):
        return self._current_winner

    def place_bid(self, bid: Bid) -> None:
        if bid.price <= self.current_price:
            print(f"Bid Price cannot be lower than current price of Rs. {self._current_price}")
            return
        if time.time() >= self.end_time or self._status != AuctionStatus.ACTIVE:
            print(f"The auction has already ended.")
            return
        print(f"User {bid.user_id} has placed a bid for {bid.price}.")
        self._current_price = bid.price
        self._current_winner = bid.user_id