import os
from typing import List
from parking_lot import ParkingLot
from vehicle import Vehicle
from car import Car
from truck import Truck
from bike import Bike

from uuid import uuid4
from random import choice

VEHICLE_COUNT = 39

class Main():

    def __init__(self):
        pass

    def run(self):
        self.parking_lot = ParkingLot()
        self.parking_lot_2 = ParkingLot()
        
        self.vehicleCount: int= VEHICLE_COUNT
        self.vehicles: List[Vehicle]= []

        self.parking_lot.addParkingLevel(numSpots=10)
        self.parking_lot.addParkingLevel(numSpots=10)
        self.parking_lot.addParkingLevel(numSpots=10)
        self.parking_lot.addParkingLevel(numSpots=10)

        for _ in range(VEHICLE_COUNT):
            vehicle = choice([
                Car(registrationNumber=str(uuid4())[:6]),
                Truck(registrationNumber=str(uuid4())[:6]),
                Bike(registrationNumber=str(uuid4())[:6])
            ])
            self.parking_lot.park(vehicle=vehicle)
            self.vehicles.append(vehicle)

        # self.parking_lot.showSummary()
        car = Car(registrationNumber=str(uuid4())[:6])
        bike = Bike(registrationNumber=str(uuid4())[:6])

        # Parking will be successful!
        self.parking_lot.park(vehicle=car)
        self.parking_lot.showSummary()

        # Parking will fail!
        self.parking_lot.park(vehicle=bike)

        # Parking will now be successful!
        self.parking_lot.unpark(vehicle=car)
        self.parking_lot.park(vehicle=bike)

        self.parking_lot.showSummary()

        print(self.parking_lot is self.parking_lot_2)
        print(id(self.parking_lot))
        print(id(self.parking_lot_2))

if __name__ == "__main__":
    Main().run()