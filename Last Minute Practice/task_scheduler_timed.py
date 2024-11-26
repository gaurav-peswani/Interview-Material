

from concurrent.futures import thread
from random import randint
from threading import Thread, Lock, Condition, get_native_id
from time import sleep, time, strftime
from heapq import heappush, heappop

class ScheduledExecutorService:

    def __init__(self) -> None:
        self._task_queue = []

        self._lock = Lock()
        self._condition = Condition(self._lock)

    def schedule(self, id: int, task: 'Callable', delay: int) -> None:
        with self._lock:
            scheduled_time = time() + delay
            print(f"[{strftime('%H:%M:%S')}] Task-{id} is scheduled to run with delay {delay}.")
            heappush(self._task_queue, (scheduled_time, id, task, None, 'ONE'))
            self._condition.notify()

    def schedule_with_fixed_delay(self, id: int, task: 'Callable', initial_delay: int, delay: int) -> None:
        with self._lock:
            scheduled_time = time() + initial_delay
            print(f"[{strftime('%H:%M:%S')}] Task-{id} is scheduled to run with delay {initial_delay} every {delay} seconds.")
            heappush(self._task_queue, (scheduled_time, id, task, delay, 'DELAY'))
            self._condition.notify()

    def schedule_with_fixed_rate(self, id: int, task: 'Callable', initial_delay: int, period: int) -> None:
        with self._lock:
            scheduled_time = time() + initial_delay
            print(f"[{strftime('%H:%M:%S')}] Task-{id} is scheduled to run with delay {initial_delay} every {period} seconds.")
            heappush(self._task_queue, (scheduled_time, id, task, period, 'RATE'))
            self._condition.notify() 

    def execute(self) -> None:
        while True:
            with self._lock:
                current_time = time()

                while not self._task_queue:
                    self._condition.wait()

                # pop from the queue
                scheduled_time, id, task, interval, schedule_type = heappop(self._task_queue)
            
            if current_time < scheduled_time:
                sleep(scheduled_time - current_time)

            # execute the task
            print(f"[Worker-{get_native_id()}] [{strftime('%H:%M:%S')}] Task-{id} is being executed.")
            task()
            print(f"[Worker-{get_native_id()}] [{strftime('%H:%M:%S')}] Task-{id} completed.")

            current_time = time()

            if schedule_type == "ONE":
                # do nothing
                pass
            elif schedule_type == "RATE":
                next_execution = scheduled_time + interval
                if next_execution <= current_time:
                    next_execution = current_time
                with self._lock:
                    heappush(self._task_queue, (next_execution, id, task, interval, schedule_type))    
            elif schedule_type == "DELAY":
                next_execution = time() + interval
                with self._lock:
                    heappush(self._task_queue, (next_execution, id, task, interval, schedule_type))

                # notify any waiting threads
                # self._condition.notify_all()

if __name__ == "__main__":

    service = ScheduledExecutorService()

    for _ in range(3):    
        executor = Thread(target=service.execute)
        executor.start()

    def task():
        sleep(4)

    threads = [
        Thread(target=service.schedule, args=(1, task, randint(1, 5))),
        Thread(target=service.schedule_with_fixed_rate, args=(2, task, 5, 2)),
        Thread(target=service.schedule_with_fixed_delay, args=(3, task, 5, 2))
    ]

    [thr.start() for thr in threads]
    [thr.join() for thr in threads]
