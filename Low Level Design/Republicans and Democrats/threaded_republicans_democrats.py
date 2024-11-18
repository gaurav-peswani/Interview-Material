from threading import Lock, Condition, Thread
import time
import random

class Bathroom:
    def __init__(self):
        self.bathRoomState = -1  # -1: empty, 0: Democrat, 1: Republican
        self.n_democrats_active = 0
        self.n_republicans_active = 0
        self.n_democrats_waiting = 0
        self.n_republicans_waiting = 0
        self.lock = Lock()
        self.democrat_condition = Condition(self.lock)
        self.republican_condition = Condition(self.lock)

    def process_democrat(self):
        with self.lock:
            if self.bathRoomState == -1 or (self.bathRoomState == 0 and self.n_democrats_active < 3):
                self.n_democrats_active += 1
                self.bathRoomState = 0
            else:
                self.n_democrats_waiting += 1
                while self.bathRoomState != -1 and (self.bathRoomState != 0 or self.n_democrats_active >= 3):
                    self.democrat_condition.wait()
                self.n_democrats_waiting -= 1
                self.n_democrats_active += 1
                self.bathRoomState = 0
        
        print(f"Democrat using the bathroom. Active Democrats: {self.n_democrats_active}")
        time.sleep(random.uniform(0.1, 1))  # Simulate bathroom usage

        with self.lock:
            self.n_democrats_active -= 1
            if self.n_democrats_active == 0 and self.n_republicans_waiting > 0:
                self.bathRoomState = 1
                for _ in range(self.n_republicans_waiting):
                    self.republican_condition.notify()
            elif self.n_democrats_active == 0:
                self.bathRoomState = -1
            elif self.n_democrats_waiting > 0:
                self.democrat_condition.notify()

    def process_republican(self):
        with self.lock:
            if self.bathRoomState == -1 or (self.bathRoomState == 1 and self.n_republicans_active < 3):
                self.n_republicans_active += 1
                self.bathRoomState = 1
            else:
                self.n_republicans_waiting += 1
                while self.bathRoomState != -1 and (self.bathRoomState != 1 or self.n_republicans_active >= 3):
                    self.republican_condition.wait()
                self.n_republicans_waiting -= 1
                self.n_republicans_active += 1
                self.bathRoomState = 1
        
        print(f"Republican using the bathroom. Active Republicans: {self.n_republicans_active}")
        time.sleep(random.uniform(0.1, 1))  # Simulate bathroom usage

        with self.lock:
            self.n_republicans_active -= 1
            if self.n_republicans_active == 0 and self.n_democrats_waiting > 0:
                self.bathRoomState = 0
                for _ in range(self.n_democrats_waiting):
                    self.democrat_condition.notify()
            elif self.n_republicans_active == 0:
                self.bathRoomState = -1
            elif self.n_republicans_waiting > 0:
                self.republican_condition.notify()


# Testing the Bathroom class
if __name__ == "__main__":
    bathroom = Bathroom()

    def democrat_thread():
        bathroom.process_democrat()

    def republican_thread():
        bathroom.process_republican()

    threads = []
    for _ in range(10):
        threads.append(Thread(target=democrat_thread))
        threads.append(Thread(target=republican_thread))

    for thread in threads:
        thread.start()

