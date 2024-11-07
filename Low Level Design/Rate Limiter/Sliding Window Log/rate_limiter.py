from urllib import request
from window import Window
from response_codes import Responses

from threading import Thread, Lock

import time

WINDOW_SIZE_SECONDS = 5
MAX_REQUESTS = 2

class RateLimiter:

    def __init__(self, window: Window):
        self.window = window
        # self.lock = Lock()

    def receive_request(self, request_id: int) -> dict:
        request_accepted = self.window.process_request(request_id=request_id)
        if request_accepted:
            return self.__allow_request()
        return self.__deny_request()

    def __allow_request(self) -> dict:
        status_code, message = Responses.HTTP_OK.value
        return {
            "status": status_code,
            "message": message
        }

    def __deny_request(self) -> dict:
        status_code, message = Responses.HTTP_REJECT.value
        return {
            "status": status_code,
            "message": message
        }
    
if __name__ == "__main__":

    window = Window(window_size=WINDOW_SIZE_SECONDS, max_requests=MAX_REQUESTS)

    rate_limiter = RateLimiter(window=window)

    start_time = time.perf_counter()
    request_id = 1
    while True:
        response = rate_limiter.receive_request(request_id=request_id)
        print(f"[{round(time.perf_counter() - start_time, 0)}] Response for Request ID {request_id}: {response}")
        if response['status'] == Responses.HTTP_OK.value[0]:
            request_id += 1
        time.sleep(0.5)