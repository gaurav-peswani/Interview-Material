from threading import Thread, Lock, Condition, Event
from time import sleep, time
from heapq import heappush, heappop
from random import randint, uniform

class RequestScheduler:

    def __init__(self) -> None:
        self.request_queue = []
    
        self._lock = Lock()
        self._condition = Condition(self._lock)
        self._stop_event = Event()

        self.request_count = 0

    def accept_request(self, name: str, priority: int) -> None:
        with self._lock:
            self.request_count += 1
            print(f"Request {name} with priority {priority} is being added to the queue")
            heappush(self.request_queue, (-priority, time(), name))
            self._condition.notify()

    def process_request(self) -> None:
        while True:
            with self._lock:
                while not self.request_queue and not self._stop_event.is_set():
                    self._condition.wait()
                if not self.request_queue and self._stop_event.is_set():
                    break
                p, _, n = heappop(self.request_queue)
                self.request_count -= 1
                print(f"Processing request {n} with priority {-p}")
            
            sleep(1) # task processing
        
        print("All tasks complete. Scheduler stopping!")

    def stop(self):
        self._stop_event.set()


if __name__ == "__main__":

    rs = RequestScheduler()

    processor = Thread(target=rs.process_request)
    processor.start()

    requests = []
    for id in range(1, 11):
        thr = Thread(target=rs.accept_request, args=(f"req-{id}", randint(1, 3)))
        thr.start()
        requests.append(thr)
        sleep(uniform(0, 1))

    [request.join() for request in requests]

    rs.stop()
    processor.join()




