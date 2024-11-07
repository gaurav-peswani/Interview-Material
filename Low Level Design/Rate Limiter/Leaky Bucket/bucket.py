from collections import deque

class Bucket:

    def __init__(self, max_requests: int):
        self.max_requests = max_requests
        self.request_queue = deque()

    def put_request(self, request_id: int) -> None:
        if len(self.request_queue) == self.max_requests:
            return False
        self.request_queue.append(request_id)
        # Process request
        return True

    def pop_requests(self, number_requests: int) -> list:
        requests = []
        while self.request_queue and number_requests:
            requests.append(str(self.request_queue.popleft()))
            number_requests -= 1
        return requests
