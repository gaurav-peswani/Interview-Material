from user import User
from flight import Flight
from booking_status import BookingStatus

class Booking:

    def __init__(self, id, user: User, flight: Flight, date: str, price: float):
        self.id = id
        self.user = user
        self.flight = flight
        self.date = date
        self.price = price
        self.status = BookingStatus.PAYMENT_PENDING

    def confirm_booking(self) -> None:
        self.status = BookingStatus.CONFIRMED