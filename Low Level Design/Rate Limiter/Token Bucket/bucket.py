class Bucket:

    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
        self.current_tokens = 0

    def put_tokens(self, token_count: int) -> None:
        self.current_tokens += token_count
        self.current_tokens = min(self.current_tokens, self.max_tokens)

    def pop_token(self) -> bool:
        if self.current_tokens > 0:
            self.current_tokens -= 1
            return True
        return False
