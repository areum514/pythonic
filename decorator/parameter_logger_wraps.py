import time
import datetime
from functools import wraps


def mesure_run_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("%s' function running time %d" %
              (func.__name__, round((end-start), 2)))
        return result

    return wrapper


def parameter_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print("[%s] args: %s, kwargs: %s" % (timestamp, args, kwargs))
        return func(*args, **kwargs)
    return wrapper


@mesure_run_time
@parameter_logger
def work(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    work(4)
