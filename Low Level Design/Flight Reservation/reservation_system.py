from typing import List
from uuid import uuid4
from user import User
from flight import Flight
from booking import Booking


class FlightReservationSystem:

    _instance = None

    def __new__(cls) -> None:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.flights = {}
            cls._instance.users = {}
            cls._instance.bookings = {}
        return cls._instance
    
    @staticmethod
    def get_instance() -> None:
        if FlightReservationSystem._instance is None:
            FlightReservationSystem()
        return FlightReservationSystem._instance
    
    def add_user(self, user: User) -> None:
        self.users[user.id] = user

    def add_flight(self, flight: Flight) -> None:
        self.flights[flight.id] = flight

    def search_flights(self, date: str, source: str, destination: str, seats: int) -> List[Flight]:
        available_flights = []
        for flight in self.flights.values():
            if flight.source == source and \
                flight.destination == destination and \
                flight.date == date and \
                self.__are_seats_available(flight, seats):
                available_flights.append(flight)
        return available_flights
    
    def __are_seats_available(self, flight: Flight, num_seats: int) -> bool:
        return len(flight.get_available_seats()) >= num_seats
    
    def __generate_booking_id(self) -> str:
        return str(uuid4)
            
    def book_flight(self, user: User, flight: Flight, seats: List[str]) -> Booking:
        for seat_number in seats:
            if not flight.is_seat_available(seat_number):
                raise Exception(f"Seat {seat_number} is not available. Please select an available seat.")
        booking_id = self.__generate_booking_id()
        booking = Booking(
            id=booking_id,
            user=user,
            flight=flight,
            date=flight.date,
            price=flight.price
        )
        flight.book_seats(seats)
        self.bookings[booking_id] = booking
        return booking

