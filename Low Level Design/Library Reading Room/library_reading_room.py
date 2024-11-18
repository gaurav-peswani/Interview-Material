from threading import Lock, Thread, get_native_id, Condition
import time

SEATS = 4

class Library:

    def __init__(self) -> None:
        self.state = "EMPTY"  # (EMPTY | READING | CLEANING)
        self.active_readers = 0
        self.waiting_readers = 0
        self.active_cleaner = False
        self.waiting_cleaners = 0

        self._lock = Lock()
        self._reader_condition = Condition(self._lock)
        self._cleaner_condition = Condition(self._lock)

    def reader_enters(self) -> None:
        with self._lock:
            if self.state == "EMPTY" or (self.state == "READING" and self.active_readers < SEATS):
                self.active_readers += 1
                self.state = "READING"
                print(f"Reader-{get_native_id()} has entered the room.")
            else:
                self.waiting_readers += 1
                print(f"Reader-{get_native_id()} is waiting.")
                while self.state != "EMPTY" or (self.state == "READING" and self.active_readers >= SEATS):
                    self._reader_condition.wait()
                self.waiting_readers -= 1
                self.active_readers += 1
                self.state = "READING"
                print(f"Reader-{get_native_id()} has entered the room.")
        
        time.sleep(2)  # Simulate library usage
        
        self.reader_leaves()

    def reader_leaves(self) -> None:
        with self._lock:
            print(f"Reader-{get_native_id()} is leaving.")
            self.active_readers -= 1
            if self.active_readers == 0:
                self.state = "EMPTY"
            if self.waiting_cleaners:
                self._cleaner_condition.notify()
            elif self.waiting_readers > 0:
                self._reader_condition.notify()  # Notify one waiting reader

    def cleaner_enters(self) -> None:
        with self._lock:
            if self.state == "EMPTY" and not self.active_cleaner:
                self.active_cleaner = True
                self.state = "CLEANING"
                print(f"Cleaner-{get_native_id()} has entered the room.")
            else:
                self.waiting_cleaners += 1
                print(f"Cleaner-{get_native_id()} is waiting.")
                while self.state != "EMPTY" or self.active_cleaner:
                    self._cleaner_condition.wait()
                self.waiting_cleaners -= 1
                self.active_cleaner = True
                self.state = "CLEANING"
                print(f"Cleaner-{get_native_id()} has entered the room.")
        
        time.sleep(2)  # Simulate cleaning process

        self.cleaner_leaves()

    def cleaner_leaves(self) -> None:
        with self._lock:
            print(f"Cleaner-{get_native_id()} is leaving.")
            self.active_cleaner = False
            self.state = "EMPTY"
            if self.waiting_readers:
                self._reader_condition.notify()  # Notify one waiting reader
            elif self.waiting_cleaners:
                self._cleaner_condition.notify()  # Notify one waiting cleaner


if __name__ == "__main__":

    library = Library()

    threads = []

    for _ in range(10):  # Create 10 reader threads
        thr = Thread(target=library.reader_enters)
        threads.append(thr)

    for _ in range(4):  # Create 4 cleaner threads
        thr = Thread(target=library.cleaner_enters)
        threads.append(thr)

    [thr.start() for thr in threads]

    [thr.join() for thr in threads]
