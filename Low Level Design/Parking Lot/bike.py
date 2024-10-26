from vehicle import Vehicle
from vehicle_type import VehicleType

class Bike(Vehicle):

    def __init__(self, registrationNumber):
        super().__init__(registrationNumber, vehicleType=VehicleType.BIKE)