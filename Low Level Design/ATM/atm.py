from heapq import heappush, heappop
from threading import Thread, Lock, Condition, Event
from random import randint
import time

class ATM:

    def __init__(self) -> None:
        self.atm_queue = []  # Priority queue
        self._lock = Lock()
        self._condition = Condition(self._lock)
        self._event = Event()
        self.active_customers = 0  # Track active customer threads

    def customer_arrival(self, priority: int, id: int) -> None:
        with self._lock:
            print(f"{time.strftime('%H:%M:%S')} - Customer-{id} with priority {priority} has arrived")
            heappush(self.atm_queue, (-priority, id))
            self.active_customers += 1
            self._condition.notify()

    def serve_customer(self) -> None:
        while not self._event.is_set() or self.atm_queue:
            with self._lock:
                while not self.atm_queue and not self._event.is_set():
                    self._condition.wait()
                if not self.atm_queue:
                    continue
                pr, id = heappop(self.atm_queue)
                print(f"{time.strftime('%H:%M:%S')} - Customer-{id} is being served with priority {-pr}.")
            time.sleep(0.5)  # Simulate service time
            with self._lock:
                self.active_customers -= 1
                if self.active_customers == 0:
                    self._condition.notify_all()

    def stop(self) -> None:
        with self._lock:
            self._event.set()
            self._condition.notify_all()  # Wake up server thread if waiting

if __name__ == "__main__":

    atm = ATM()

    # Start server thread
    server = Thread(target=atm.serve_customer)
    server.start()

    # Create customer threads
    customers = []
    for id in range(10):
        pr = randint(1, 3)
        thr = Thread(target=atm.customer_arrival, args=(pr, id))
        customers.append(thr)
        thr.start()
        time.sleep(0.1)  # Simulate staggered arrival times

    # Wait for all customer threads to finish
    [thr.join() for thr in customers]

    # Wait for the server thread to finish processing the queue
    with atm._lock:
        while atm.active_customers > 0:
            atm._condition.wait()

    # Stop the server thread
    atm.stop()
    server.join()
