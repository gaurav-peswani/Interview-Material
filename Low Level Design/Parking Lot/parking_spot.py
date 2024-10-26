"""
* Each parking spot should be able to accommodate a specific type of vehicle.
* The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
"""
from vehicle import Vehicle

class ParkingSpot():
    
    def __init__(self, spotNumber: int):
        self.spotNumber: int = spotNumber
        self.occupied: bool = False
        self.parkedVehicle: Vehicle = None

    def park(self, vehicle: Vehicle):
        self.parkedVehicle = vehicle
        self.occupied = True

    def unpark(self):
        self.parkedVehicle = None
        self.occupied = None

    def __repr__(self):
        return f"Spot [{self.spotNumber}]: {self.parkedVehicle}"
