import time
from functools import wraps


class MesureRuntime:
    def __init__(self, active_state):
        self.mesure_active = active_state

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.mesure_active is False:
                return func(*args, **kwargs)
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(
                f"'{func.__name__}' function running time {round((end-start),2)}")
            return result
        return wrapper


@MesureRuntime(True)
def active_worker(delay_time):
    time.sleep(delay_time)


@MesureRuntime(False)
def non_active_worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    active_worker(3)
    non_active_worker(3)
