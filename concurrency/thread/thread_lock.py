import time
import logging
import threading

logging.basicConfig(level=logging.DEBUG, format="(%(threadName)s)%(message)s")


def blocking_lock(lock):
    logging.debug("Start blocking lock")

    while True:
        """ time.sleep(1)
        lock.acquire() #락 잡기
        try:
            logging.debug("Grab it")
            time.sleep(0.5)
        finally:
            logging.debug("Release")
            lock.release() #락풀기 """
        time.sleep(1)
        with lock:
            logging.debug("Grab it")
            time.sleep(0.5)
        """same..!! but only can use blocking lock if you want to use with non-blocking lock inheritance will can use it
        """


def nonblocking_lock(lock):
    logging.debug("Start nonblocking lock")

    attempt, grab = 0, 0
    while grab < 3:
        time.sleep(1)
        logging.debug("Attempt")
        success = lock.acquire(False)

        try:
            attempt += 1
            if success:
                logging.debug("Grap it")
                grab += 1
        finally:
            if success:
                logging.debug("Release")
                lock.release()
    logging.debug("Attempt : %s, grab: %s" % (attempt, grab))


def main():
    lock = threading.Lock()

    blocking = threading.Thread(
        target=blocking_lock, name="blocking", args=(lock,))
    blocking.setDaemon(True)
    blocking.start()

    nonblocking = threading.Thread(
        target=nonblocking_lock, name="nonblocking", args=(lock,))
    nonblocking.start()


if __name__ == "__main__":
    main()
