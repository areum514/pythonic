msg = "hello"


def write():
    global msg
    msg += " world"
    print(msg)


def main():
    print("===print msg===")
    print(msg)

    print("===write funcion===")
    write()

    print("===print msg===")
    print(msg)


if __name__ == "__main__":
    main()
