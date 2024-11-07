from collections import deque
import time

class Window:

    def __init__(self, window_size: int, max_requests: int):
        self.queue = deque()
        self.window_size = window_size
        self.max_requests = max_requests

    def process_request(self, request_id: int) -> bool:
        curr_time = time.time()
        if self.queue and round(curr_time - self.queue[0][0], 0) >= self.window_size:
            request_time, request_id = self.queue.popleft()
            print(f"Request with ID {request_id} was made {round(curr_time - request_time, 0)} seconds ago and is being removed from the queue.")
        if len(self.queue) == self.max_requests:
            return False
        self.queue.append((time.time(), request_id))
        return True
        
            