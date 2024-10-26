"""
* The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
"""

from vehicle_type import VehicleType
from abc import ABC

class Vehicle(ABC):

    def __init__(self, registrationNumber: str, vehicleType: VehicleType):
        self.registrationNumber = registrationNumber
        self.vehicleType = vehicleType

    def __repr__(self):
        return f"[ {self.vehicleType.name} | {self.registrationNumber} ]\n"

    

