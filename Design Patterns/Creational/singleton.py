"""
Singleton Pattern: 
 * [Single Instance] Ensure that a class has only one instance throughout the lifetime of the application
 * [Global Point of Access] Commonly used in cases where a single resource needs to be shared across the 
    entire system, such as a database connection, logging service, or configuration object.
"""

from threading import Lock, Thread

class SingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(self.value)

if __name__ == "__main__":
    process_1 = Thread(target=Singleton(10).print_value).start()
    process_2 = Thread(target=Singleton(20).print_value).start()

    print(Singleton(10) is Singleton(20))
        
    