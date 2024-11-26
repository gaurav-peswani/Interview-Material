from heapq import heappush, heappop
from threading import Thread, Condition, Event, Lock, get_native_id
from time import sleep, time, strftime
from random import randint, uniform
from datetime import datetime

TIERS = {
    1: "PLATINUM",
    2: "GOLD",
    3: "SILVER"
}
WORKERS = 3

class BackupService:

    def __init__(self) -> None:
        self.request_queue = []
        
        self._lock = Lock()
        self._condition = Condition(self._lock)
        self._stop_event = Event()


    def accept_request(self, name: str, priority: int) -> None:
        with self._lock:
            print(f"Request {name} with priority {TIERS[priority]} is accepted.")
            heappush(self.request_queue, (priority, time(), name))
            self._condition.notify()

    def process_request(self) -> None:
        while True:
            with self._lock:
                while not self.request_queue and not self._stop_event.is_set():
                    self._condition.wait()
                if not self.request_queue and self._stop_event.is_set():
                    break
                p, at, n = heappop(self.request_queue)
                
            start = time()
            start_str = datetime.fromtimestamp(start).strftime("%H:%M:%S")            
            sleep(uniform(3, 5)) # processing task
            
            end = time()
            end_str = datetime.fromtimestamp(start).strftime("%H:%M:%S")
            print(f">>> [Worker-{get_native_id()}] [{end_str}] Request {n} {TIERS[p]} took {end - start} second(s).")


    def stop(self) -> None:
        self._stop_event.set()


if __name__ == "__main__":

    backup = BackupService()

    threads = []
    for _ in range(WORKERS):
        thr = Thread(target=backup.process_request)
        thr.start()
        threads.append(thr)

    for id in range(1, 21):
        name = f"request-{id}"
        priority = randint(1, 3)
        thr = Thread(target=backup.accept_request, args=(name, priority))
        thr.start()
        sleep(0.2)
        threads.append(thr)
    sleep(5)
    for id in range(21, 41):
        name = f"request-{id}"
        priority = randint(1, 3)
        thr = Thread(target=backup.accept_request, args=(name, priority))
        thr.start()
        sleep(0.2)
        threads.append(thr)


    backup.stop()
    [thr.join() for thr in threads]
