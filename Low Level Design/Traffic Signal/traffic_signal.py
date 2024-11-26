from threading import Condition, Thread, Lock
from time import sleep
import time

class TrafficSignal:

    def __init__(self) -> None:
        self.ns_pedestrians_travelling = 0
        self.ns_pedestrians_waiting = 0

        self.ew_pedestrians_travelling = 0
        self.ew_pedestrians_waiting = 0

        self.intersection = "NS"

        self.ns_light = "GREEN"
        self.ew_light = "RED"

        self._lock = Lock()
        self.ns_cond = Condition(self._lock)
        self.ew_cond = Condition(self._lock)

    def ns_pedestrian(self) -> None:
        with self._lock:
            if self.ns_light == "GREEN":
                self.ns_pedestrians_travelling += 1
            else:
                while self.ns_light != "GREEN":
                    self.ns_cond.wait()
                self.ns_light = "GREEN"
                self.ns_pedestrians_waiting -= 1
                self.ns_pedestrians_travelling += 1

        with self._lock:
            self.ns_pedestrians_travelling -= 1
            if self.ns_pedestrians_travelling == 0:
                self.ns_light = "YELLOW"
        
        time.sleep(2)

        with self._lock:
            if 