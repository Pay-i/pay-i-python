import time


class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.perf_counter()

    def stop(self):
        self.end_time = time.perf_counter()

    def elapsed_s(self):
        if self.start_time is None:
            raise ValueError("Stopwatch has not been started")
        if self.end_time is None:
            return time.perf_counter() - self.start_time
        return self.end_time - self.start_time

    def elapsed_ms(self):
        return self.elapsed_s() * 1000

    def elapsed_ms_int(self):
        return int(self.elapsed_ms())

