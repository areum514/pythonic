import time


def measure_run_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}, {round((end-start),2)}")
        return result

    return wrapper


@measure_run_time
def worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(3)
