from vehicle import Vehicle
from vehicle_type import VehicleType

class Bike(Vehicle):

    def __init__(self, registrationNumber):
        super().__init__(registrationNumber, vehicleType=VehicleType.BIKE)

    def __is_bike_available(self) -> None:
        return None