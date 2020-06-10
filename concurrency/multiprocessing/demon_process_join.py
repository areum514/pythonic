import time
import multiprocessing


def daemon():
    print("Strat")
    time.sleep(5)
    print("Exit")


def main():
    d = multiprocessing.Process(target=daemon, name="daemon")

    d.daemon = True

    d.start()
    d.join()


if __name__ == "__main__":
    main()
