"""
* The parking lot should have multiple levels, each level with a certain number of parking spots.
"""

from typing import List

from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingLevel():

    def __init__(self, levelNumber: int, numSpots: int):
        self.levelNumber = levelNumber
        self.numSpots = numSpots
        self.spots : List[ParkingSpot] = []

        for id in range(1, self.numSpots + 1):
            self.spots.append(ParkingSpot(spotNumber=id))

    def park(self, vehicle: Vehicle) -> bool:
        for spot in self.spots:
            if not spot.occupied:
                spot.park(vehicle=vehicle)
                return True
        return False
    
    def unpark(self, vehicle: Vehicle) -> bool:
        for spot in self.spots:
            if spot.occupied and spot.parkedVehicle == vehicle:
                spot.unpark()
                return True
        return False
    
    def getFreeSpots(self) -> int:
        freeSpots = 0
        for spot in self.spots:
            if not spot.occupied:
                freeSpots += 1
        return freeSpots
    
    def getOccupiedSpots(self) -> int:
        occupiedSpots = 0
        for spot in self.spots:
            if spot.occupied:
                occupiedSpots += 1
        return occupiedSpots
    
    def __repr__(self):
        return f"**** Level [{self.levelNumber}] ****"

    