import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s) %(message)s")
RESOURCE = 0


def set_reverse(lock):
    logging.debug("Start batch")
    with lock:
        logging.debug("Grab lock!")

        if RESOURCE == 0:
            set_one(lock, True)
        else:
            set_zero(lock, True)
    logging.debug("Reversed")


def set_zero(lock, end=False):
    logging.debug("Start set zero")

    while True:
        with lock:
            logging.debug("Grab lock and set RESEURCE to 0.")
            RESOURCE = 0
            time.sleep(0.5)
        time.sleep(1)
        if end:
            break
