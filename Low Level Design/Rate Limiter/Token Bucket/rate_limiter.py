import time

from threading import Thread, Lock

from urllib import request
from bucket import Bucket
from response_codes import Responses

MAX_TOKENS = 20
TOKEN_REFILL_INTERVAL_SECONDS = 10
TOKEN_REFILL_AMOUNT = 2

class RateLimiter:

    def __init__(self, bucket: Bucket):
        self.bucket = bucket
        self.lock = Lock()
        pass

    def __is_token_available(self) -> bool:
        with self.lock:
            return self.bucket.pop_token()

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

    def receive_request(self):
        if self.__is_token_available():
            return self.__allow_request()
        return self.__deny_request()
    
    def add_tokens(self, token_count: int=TOKEN_REFILL_AMOUNT, interval: int=TOKEN_REFILL_INTERVAL_SECONDS):
        while True:
            curr_time = time.perf_counter()
            with self.lock:
                self.bucket.put_tokens(token_count=token_count)
            print(f"[{round(curr_time, 0)}] Added {token_count} token(s) into the bucket.")
            time.sleep(interval)            


if __name__ == "__main__":
    # Initialize the bucket
    bucket = Bucket(max_tokens=MAX_TOKENS)

    # Initialize the rate limiter
    rate_limiter = RateLimiter(bucket=bucket)

    # keep filling 2 token(s) every 5 seconds
    rate_limiter_refiller = Thread(target=rate_limiter.add_tokens)
    rate_limiter_refiller.start()

    # make requests
    while True:
        curr_time = time.perf_counter()
        response = rate_limiter.receive_request()
        print(f"[{round(curr_time, 0)}] Response from Rate Limiter: {response}")
        time.sleep(1)
