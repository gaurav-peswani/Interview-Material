from heapq import heappush, heappop
from threading import Thread, Condition, Lock
from random import randint
import time

class PrintScheduler:

    def __init__(self) -> None:
        self.task_queue = [] # (priority, message)
        self._lock = Lock()
        self._condition = Condition(self._lock)

    def schedule_print(self, priority: int, message: str) -> None:
        with self._lock:
            heappush(self.task_queue, (-priority, message))
            self._condition.notify()

    def execute_print(self) -> None:
        while True:
            with self._lock:
                while not self.task_queue:
                    self._condition.wait()
                _, message = heappop(self.task_queue)
                print(message)

if __name__ == "__main__":

    scheduler = PrintScheduler()

    executor = Thread(target=scheduler.execute_print)
    executor.start()
    
    printers = []
    for id in range(5):
        prio = randint(1, 2)
        message = f"This is message-{id}"
        print(f"[{prio}] {message}")
        thr = Thread(target=scheduler.schedule_print, args=(prio, message))
        printers.append(thr)

    [thr.start() for thr in printers]
    [thr.join() for thr in printers]