from flight import Flight
from booking import Booking
from user import User
from seat import Seat
from reservation_system import FlightReservationSystem

if __name__ == "__main__":

    flight_reservation_system = FlightReservationSystem.get_instance()

    user_1 = User("1", "Gaurav", "a@gmail.com", "99999-99999")
    user_2 = User("1", "Rohan", "b@gmail.com", "99999-99997")
    user_3 = User("1", "Vipul", "c@gmail.com", "99999-99998")

    flights = [
        Flight("1", "DEL", "BLR", "AI-321", "06-11-2024", "10:00", "12:30", 2500.00),
        Flight("2", "DEL", "BLR", "AI-324", "06-11-2024", "01:00", "03:30", 3000.00),
        Flight("3", "DEL", "BLR", "AI-325", "06-11-2024", "05:00", "07:30", 3500.00),
        Flight("4", "DEL", "BLR", "AI-321", "07-11-2024", "10:00", "12:30", 3500.00),
        Flight("5", "DEL", "BLR", "AI-324", "07-11-2024", "01:00", "03:30", 4000.00),
        Flight("6", "DEL", "BLR", "AI-325", "07-11-2024", "05:00", "07:30", 5500.00)
    ]

    for flight in flights:
        flight.add_seats(2, 2)

    flight_reservation_system.add_user(user_1)
    flight_reservation_system.add_user(user_2)
    flight_reservation_system.add_user(user_3)

    for flight in flights:
        flight_reservation_system.add_flight(flight)

    available_flights = flight_reservation_system.search_flights("06-11-2024", "DEL", "BLR", 2)
    print(f"Select one of the following flights: {available_flights}")

    booking = flight_reservation_system.book_flight(user_1, flights[0], ["1-1", "1-2"])
    print(f"Booking Details: {booking}")


