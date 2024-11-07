import time

from threading import Thread, Lock

from urllib import request
from bucket import Bucket
from response_codes import Responses

REQUESTS_PER_INTERVAL = 5
REQUEST_PROCESS_INTERVAL_SECONDS = 20

class RateLimiter:

    def __init__(self, bucket: Bucket):
        self.bucket = bucket
        self.lock = Lock()
        pass

    def __allow_request(self) -> dict:
        status_code, message = Responses.HTTP_OK.value
        # Some application logic
        return {
            "status": status_code,
            "message": message,
        }

    def __deny_request(self) -> dict:
        status_code, message = Responses.HTTP_REJECT.value
        return {
            "status": status_code,
            "message": message,
        }

    def receive_request(self, request_id: int):
        requestAccepted = False
        with self.lock:
            requestAccepted = self.bucket.put_request(request_id=request_id)
        if requestAccepted:
            return self.__allow_request()
        return self.__deny_request()
    
    def process_requests(self, number_requests: int=REQUESTS_PER_INTERVAL, interval: int=REQUEST_PROCESS_INTERVAL_SECONDS):
        while True:
            curr_time = time.perf_counter()
            with self.lock:
                requests_completed = self.bucket.pop_requests(number_requests=number_requests)
            if requests_completed:
                print(f"[{round(curr_time, 0)}] Requests with IDs: {', '.join(requests_completed)} have been processed.")
            time.sleep(interval)            


if __name__ == "__main__":
    # Initialize the bucket
    bucket = Bucket(max_requests=REQUESTS_PER_INTERVAL)

    # Initialize the rate limiter
    rate_limiter = RateLimiter(bucket=bucket)

    # keep processing 5 requests every 10 seconds
    rate_limiter_processor = Thread(target=rate_limiter.process_requests)
    rate_limiter_processor.start()

    # make requests
    request_id = 1
    while True:
        curr_time = time.perf_counter()
        response = rate_limiter.receive_request(request_id=request_id)
        print(f"[{round(curr_time, 0)}] [Request ID: {request_id}] Response from Rate Limiter: {response}")
        if response['status'] != Responses.HTTP_REJECT.value[0]:
            request_id += 1
        time.sleep(1)
