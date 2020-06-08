import time
from functools import update_wrapper


class MesureRuntime:
    def __init__(self, f):
        self.func = f
        update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print(f"'{self.func.__name__}' function running time {round((end-start),2)}")
        return result


@MesureRuntime
def worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(5)
"""f = MesureRuntime(worker)
    f(5)"""
