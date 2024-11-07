from enum import Enum

class Responses(Enum):
    HTTP_OK = 200, "Successful Response"
    HTTP_REJECT = 429, "Too many requests. Please try again later"
    HTTP_ERROR = 500, "Internal Server Error"