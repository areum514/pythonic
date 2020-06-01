import datetime
import time


def logger():
    now = datetime.datetime.now()

    def print_log(msg):
        return f"{now} {msg}"

    return print_log


def main():
    log = logger()
    print(log("Start."))
    time.sleep(10)

    print(log("After 10 sec."))


# datetime.datetime.now() 실행된 값이 __closure__속성에 저장되기 떄문에
# closure를 구현할 떄는 nonlocal 변수로 시간이나 흐름에 따라 변하는 value를 사용하지 않아유~
if __name__ == "__main__":
    main()
