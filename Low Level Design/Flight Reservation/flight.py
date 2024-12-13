from typing import List
from seat import Seat

class Flight:

    def __init__(self, id: str, source: str, destination: str, aircraft: str, date: str, from_time: str, to_time: str, price: float) -> None:
        self.id = id
        self.source = source
        self.destination = destination
        self.aircraft = aircraft
        self.date = date
        self.from_time = from_time
        self.to_time = to_time
        self.price = price
        self.seats = {}

    def add_seats(self, rows: int, columns: int) -> None:
        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                seat_number = f"{r}-{c}"
                self.seats[seat_number] = Seat(seat_number=seat_number)

    def get_available_seats(self) -> List[Seat]:
        available_seats = []
        for _, seat in self.seats.items():
            if seat.is_available:
                available_seats.append(seat)
        return available_seats
    
    def is_seat_available(self, seat_number: str) -> bool:
        return self.seats[seat_number].is_available
    
    def book_seats(self, seats: List[str]) -> None:
        for seat_number in seats:
            self.seats[seat_number].book_seat()
