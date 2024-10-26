"""
* The parking lot should have multiple levels, each level with a certain number of parking spots.
"""

from typing import List, Dict
from parking_level import ParkingLevel
from parking_spot import ParkingSpot
from vehicle import Vehicle

class ParkingLot():

    _instance = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__new__(cls, *args, **kwargs)
        return cls._instance[cls]

    def __init__(self):
        self.numParkingLevels: int = 0
        self.parkingLevels: List[ParkingLevel] = []

    def addParkingLevel(self, numSpots: int):
        self.parkingLevels.append(
            ParkingLevel(
                levelNumber=self.numParkingLevels, 
                numSpots=numSpots
            ))
        self.numParkingLevels += 1

    def park(self, vehicle: Vehicle) -> bool:
        for level in self.parkingLevels:
            if level.park(vehicle=vehicle):
                return True
        print(f"Hi {vehicle.registrationNumber}! No Parking Slot available. Please try again after sometime.")
        return False
    
    def unpark(self, vehicle: Vehicle) -> bool:
        for level in self.parkingLevels:
            if level.unpark(vehicle=vehicle):
                return True
        return False
    
    def showSummary(self) -> None:
        freeSpots = 0
        occupiedSpots = 0

        for level in self.parkingLevels:
            print(level)
            for spot in level.spots:
                print(spot)
            freeSpots += level.getFreeSpots()
            occupiedSpots += level.getOccupiedSpots()

        print("Summary of the Parking Lot:\n")
        print(f"Number of Levels: {self.numParkingLevels}")
        print(f"Number of Occupied Spots: {occupiedSpots}")
        print(f"Number of Free Spots: {freeSpots}")

        return None


