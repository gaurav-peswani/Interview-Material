from threading import Lock, Thread
from time import sleep

class ReadWriteLock:

    def __init__(self) -> None:
        self._active_readers = 0
        
        self._lock = Lock()
        self._reader_lock = Lock()
        pass

    def acquire_read_lock(self) -> None:
        with self._reader_lock:
            self._active_readers += 1
            if self._active_readers == 1:
                self._lock.acquire()

    def release_read_lock(self) -> None:
        with self._reader_lock:
            self._active_readers -= 1
            if self._active_readers == 0:
                self._lock.release()

    def acquire_write_lock(self) -> None:
        self._lock.acquire()

    def release_write_lock(self) -> None:
        self._lock.release()

class Resource:

    def __init__(self) -> None:
        self.file = []
        self.rw_lock = ReadWriteLock()

    def read(self, reader_id: int) -> None:
        self.rw_lock.acquire_read_lock()
        print(f"Reader {reader_id} is reading the file.")
        sleep(1)
        print(f"File read: {self.file}")
        self.rw_lock.release_read_lock()

    def write(self, writer_id: int, data: str) -> None:
        self.rw_lock.acquire_write_lock()
        print(f"Writer {writer_id} is writing to the file.")
        self.file.append(data)
        sleep(2)
        print(f"File written: {self.file}")
        self.rw_lock.release_write_lock()

if __name__ == "__main__":

    resource = Resource()
    threads = []

    for id in range(5):
        thr = Thread(target=resource.read, args=(id, ))
        threads.append(thr)

    for id in range(5, 8):
        thr = Thread(target=resource.write, args=(id, f"I am Writer Thread-{id}"))
        threads.append(thr)

    for id in range(8, 13):
        thr = Thread(target=resource.read, args=(id, ))
        threads.append(thr)

    [thr.start() for thr in threads]

    [thr.join() for thr in threads]