class Seat:

    def __init__(self, seat_number: str) -> None:
        self.seat_number = seat_number
        self.is_available = True
        
    def book_seat(self) -> None:
        self.is_available = False
        
    def cancel_seat(self) -> None:
        self.is_available = True