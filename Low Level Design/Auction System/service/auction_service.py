import time
from threading import Thread

from enums.auction_status import AuctionStatus
from entities.auction import Auction
from entities.bid import Bid

class AuctionService:

    _instance = None

    def __new__(cls, *args, **kwargs) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
            cls._instance.auctions = {}
        return cls._instance

    @staticmethod
    def get_instance() -> 'AuctionService':
        if AuctionService._instance is None:
            AuctionService()
        return AuctionService._instance

    def create_auction(self, auction: Auction) -> None:
        self.auctions[auction.id] = auction

    def get_auction_by_id(self, auction_id: str) -> Auction:
        return self.auctions[auction_id]

    def start_auction(self, auction_id: str) -> None:
        auction = self.get_auction_by_id(auction_id)
        current_time = time.time()
        end_time = current_time + auction.duration

        self.auctions[auction_id].status = AuctionStatus.ACTIVE
        self.auctions[auction_id].end_time = end_time

        print(f"Auction {auction.id} has started. Bids valid till {end_time}.")
        print(f"Item: {auction.item}\nStarting Price: {auction.starting_price}")

    def end_auction(self, auction_id: str) -> None:
        print(f"Auction {auction_id} has ended.")
        self.auctions[auction_id].status = AuctionStatus.FINISHED

    def get_winner(self, auction_id: str) -> None:
        auction = self.get_auction_by_id(auction_id)
        if auction.current_winner is not None:
            print(f"The winner for Auction {auction_id} is {auction.current_winner} with a bid of {auction.current_price}.")
        else:
            print(f"No bidder for Auction {auction_id}.")

    def place_bid(self, auction_id: str, bid: Bid) -> None:
        auction = self.get_auction_by_id(auction_id)
        auction.place_bid(bid)