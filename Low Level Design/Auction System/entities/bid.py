class Bid:

    def __init__(self, auction_id: str, user_id: str, price: int) -> None:
        self._auction_id = auction_id
        self._user_id = user_id
        self._price = price

    @property
    def price(self):
        return self._price

    @property
    def auction_id(self):
        return self._auction_id

    @property
    def user_id(self):
        return self._user_id

