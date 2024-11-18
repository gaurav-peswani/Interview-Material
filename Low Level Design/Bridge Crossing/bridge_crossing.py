from threading import Lock, Thread, Condition, get_native_id
import time


class Bridge:

    def __init__(self) -> None:
        self.road = "EMPTY"  # (NORTH | SOUTH | EMPTY)
        self.north_travelling = 0
        self.north_waiting = 0
        self.south_travelling = 0
        self.south_waiting = 0
        self.last_served = "SOUTH"  # Start with priority for NORTH

        self._lock = Lock()
        self._north_cd = Condition(self._lock)
        self._south_cd = Condition(self._lock)

    def car_north_enters(self) -> None:
        with self._lock:
            print(f"Car North-{get_native_id()} is waiting.")
            self.north_waiting += 1
            while self.road == "SOUTH" or (
                self.road == "EMPTY" and self.last_served == "NORTH" and self.south_waiting > 0
            ):
                self._north_cd.wait()

            print(f"Car North-{get_native_id()} is travelling.")
            self.north_waiting -= 1
            self.north_travelling += 1
            self.road = "NORTH"

        time.sleep(2)  # Car travelling

        self.car_north_leaves()

    def car_north_leaves(self) -> None:
        with self._lock:
            print(f"Car North-{get_native_id()} is leaving.")
            self.north_travelling -= 1
            if self.north_travelling == 0:
                self.road = "EMPTY"
                self.last_served = "NORTH"  # Give priority to SOUTH next
                if self.south_waiting > 0:
                    self._south_cd.notify()
                elif self.north_waiting > 0:
                    self._north_cd.notify()

    def car_south_enters(self) -> None:
        with self._lock:
            print(f"Car South-{get_native_id()} is waiting.")
            self.south_waiting += 1
            while self.road == "NORTH" or (
                self.road == "EMPTY" and self.last_served == "SOUTH" and self.north_waiting > 0
            ):
                self._south_cd.wait()

            print(f"Car South-{get_native_id()} is travelling.")
            self.south_waiting -= 1
            self.south_travelling += 1
            self.road = "SOUTH"

        time.sleep(2)  # Car travelling

        self.car_south_leaves()

    def car_south_leaves(self) -> None:
        with self._lock:
            print(f"Car South-{get_native_id()} is leaving.")
            self.south_travelling -= 1
            if self.south_travelling == 0:
                self.road = "EMPTY"
                self.last_served = "SOUTH"  # Give priority to NORTH next
                if self.north_waiting > 0:
                    self._north_cd.notify()
                elif self.south_waiting > 0:
                    self._south_cd.notify()


if __name__ == "__main__":

    bridge = Bridge()
    threads = []

    for _ in range(10):  # North cars
        thr = Thread(target=bridge.car_north_enters)
        threads.append(thr)

    for _ in range(8):  # South cars
        thr = Thread(target=bridge.car_south_enters)
        threads.append(thr)

    [thr.start() for thr in threads]
    [thr.join() for thr in threads]
