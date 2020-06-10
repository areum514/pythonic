def coroutine():
    while True:
        msg = yield
        print("Hello, your input message is '%s'" % msg)


def main():
    c = coroutine()
    next(c)
    next(c)
    c.send("test")
    c.send("Coroutine")


if __name__ == "__main__":
    main()
