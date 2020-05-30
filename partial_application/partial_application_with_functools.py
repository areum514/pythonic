from functools import partial


def logging(year, month, day, title, content):
    print(f"{year}-{month}-{day},{title},{content}")


def main():

    print("=== use partial funcion===")
    f = partial(logging, "2017", "12", "28")
    f("python2", "end of support in 2020 ")
    f("python3", "updating")


if __name__ == "__main__":
    main()
