from threading import Condition, Thread, get_native_id, Lock
from collections import deque
import time
from concurrent.futures import ThreadPoolExecutor

class ThreadSafeQueue:

    def __init__(self, capacity: int) -> None:
        self.queue = deque()
        self.max_capacity = capacity
        self._lock = Lock()
        self._condition = Condition(self._lock)
        self._peekers = 0
        self._peek_lock = Lock()

    def _is_empty(self) -> bool:
        return len(self.queue) == 0
    
    def _is_full(self) -> bool:
        return len(self.queue) == self.max_capacity
    
    def _is_being_peeked(self) -> bool:
        return self._peekers > 0

    def push(self, data: int) -> None:
        with self._condition:
            while self._is_full():
                print(f"Thread-{get_native_id()} is waiting for queue to have slots.")
                self._condition.wait()
            print(f"[PUSH] Thread-{get_native_id()} acquired the lock.")
            print(f"Thread-{get_native_id()} is pushing {data} to the queue.")
            self.queue.append(data)
            time.sleep(2)
            self._condition.notify_all()
            print(f"[PUSH] Thread-{get_native_id()} released the lock.")

    def pop(self) -> int:
        with self._condition:
            while self._is_empty():
                print(f"Thread-{get_native_id()} is waiting for queue to fill slots.")
                self._condition.wait()
            print(f"[POP] Thread-{get_native_id()} acquired the lock.")
            print(f"Thread-{get_native_id()} is popping from the queue.")
            popped = self.queue.popleft()
            time.sleep(2)
            self._condition.notify_all()
            print(f"[POP] Thread-{get_native_id()} released the lock.")
            return popped
        
    def peek(self) -> int:
        with self._peek_lock:
            self._peekers += 1
            if self._peekers == 1:
                self._lock.acquire()
                print(f"[PEEK] Thread-{get_native_id()} acquired the lock.")

        
        print(f"Thread-{get_native_id()} is peeking from the queue.")
        top = -1
        if self.queue:
            top = self.queue[0]
        time.sleep(1)
    
        with self._peek_lock:
            self._peekers -= 1
            if self._peekers == 0:
                self._lock.release()
                print(f"[PEEK] Thread-{get_native_id()} released the lock.")
        
        return top

        
if __name__ == "__main__":
    queue = ThreadSafeQueue(capacity=5)
    futures = []

    with ThreadPoolExecutor(max_workers=50) as executor:
        for data in range(15):
            futures.append(executor.submit(queue.push, data))
        for _ in range(30, 40):
            futures.append(executor.submit(queue.peek))
        for _ in range(15, 30):
            futures.append(executor.submit(queue.pop))        
    
    print([future.result() for future in futures])

    