import random
from threading import Lock, Condition, Event, Thread
from time import sleep
from heapq import heappush, heappop

class TaskScheduler:

    def __init__(self) -> None:
        self.task_queue = []
        self._lock = Lock()
        self._condition = Condition(self._lock)
        self._stop_event = Event()
        self.active_tasks = 0

    def schedule_task(self, name: str, priority: int) -> None:
        with self._lock:
            print(f"Task {name} with priority {priority} added to queue.")
            heappush(self.task_queue, (-priority, name))
            self._condition.notify()

    def execute_task(self) -> None:
        while True:
            with self._lock:
                while not self.task_queue and not self._stop_event.is_set():
                    self._condition.wait()
                if self._stop_event.is_set() and not self.task_queue:
                    break
                pr, task_name = heappop(self.task_queue)
                print(f"Task {task_name} is being executed.")
            
            sleep(0.5)  # simulate task execution
            
        print("All tasks completed, shutting down executor.")

    def stop(self) -> None:
        self._stop_event.set()

if __name__ == "__main__":

    scheduler = TaskScheduler()

    executor = Thread(target=scheduler.execute_task)
    executor.start()

    tasks = []

    for id in range(1, 21):
        pr = random.randint(1, 4)
        name = f"work-{id}"
        thr = Thread(target=scheduler.schedule_task, args=(name, pr))
        tasks.append(thr)
        sleep(0.1)
        thr.start()

    [thr.join() for thr in tasks]

    # Wait until all tasks are finished
    scheduler.stop()
    executor.join()

    print("Scheduler has been stopped.")
