import time
import datetime


def mesure_run_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}' function running time {round((end-start),2)}")
        return result

    return wrapper


def parameter_logger(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        print(f"[{timestamp}] args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


@mesure_run_time
@parameter_logger
def work(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    work(4)
