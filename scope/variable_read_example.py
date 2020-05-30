msg = "hello"


def read_work():
    print(msg)
    print("World")


def read_exception():
    print(msg)
    msg = "World"
    print(msg)


def main():
    print("===first read===")
    read_work()

    print("===second read===")
    read_exception()


if __name__ == "__main__":
    main()
