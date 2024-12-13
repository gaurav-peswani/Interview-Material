import time
from concurrent.futures.thread import ThreadPoolExecutor

from service.auction_service import AuctionService
from service.user_service import UserService

from entities.user import User
from entities.auction import Auction
from entities.bid import Bid

class Demo:

    @staticmethod
    def run() -> None:

        auction_service = AuctionService.get_instance()
        user_service = UserService.get_instance()

        user1 = User("A", "User A", "password_a")
        user2 = User("B", "User B", "password_b")
        user3 = User("C", "User C", "password_c")
        user4 = User("D", "User D", "password_d")
        user_service.add_user(user1)
        user_service.add_user(user2)
        user_service.add_user(user3)
        user_service.add_user(user4)

        auction1 = Auction("0001", "Painting", "Monalisa Painting", 10000, 20, user1.id)
        auction_service.create_auction(auction1)
        auction_service.start_auction(auction1.id)

        bid1 = Bid(auction1.id, user2.id, 11000)
        auction_service.place_bid(auction1.id, bid1)
        time.sleep(2)

        bid2 = Bid(auction1.id, user3.id, 12000)
        auction_service.place_bid(auction1.id, bid2)
        time.sleep(2)

        bid3 = Bid(auction1.id, user4.id, 13000)
        auction_service.place_bid(auction1.id, bid3)
        time.sleep(2)

        bid4 = Bid(auction1.id, user2.id, 14000)
        auction_service.place_bid(auction1.id, bid4)
        time.sleep(2)

        bid5 = Bid(auction1.id, user3.id, 15000)
        auction_service.place_bid(auction1.id, bid5)
        time.sleep(2)

        bid6 = Bid(auction1.id, user4.id, 16000)
        auction_service.place_bid(auction1.id, bid6)

        auction_service.end_auction(auction1.id)

        auction_service.get_winner(auction1.id)

if __name__ == "__main__":
    Demo.run()