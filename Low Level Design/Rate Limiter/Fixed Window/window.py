import time


class Window:

    def __init__(self, window_size:int, max_requests:int):
        self.window_size = window_size
        self.max_requests = max_requests
        self.requests_received = 0
        self.window_start_time = time.perf_counter()

    def process_request(self) -> bool:
        current_time = time.time()
        print(f"Current Time: {current_time}, Start Time: {self.window_start_time}, Diff: {round(current_time - self.window_start_time, 0)}")
        if round(current_time - self.window_start_time, 0) <= self.window_size and self.requests_received == self.max_requests:
            return False
        elif current_time > self.window_start_time + self.window_size:
            self.window_start_time = current_time
            self.requests_received = 0
        self.requests_received += 1
        return True
