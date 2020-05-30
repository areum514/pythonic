def partial(func, *partial_args):
    def wrapper(*extra_args):
        args = list(partial_args)
        args.extend(extra_args)
        return func(*args)
    return wrapper


def logging(year, month, day, title, content):
    print(f"{year}-{month}-{day},{title},{content}")


def main():
    print("=== use logging funcion===")
    logging("2017", "12", "28", "python2", "end of support in 2020 ")
    logging("2017", "12", "28", "python3", "updating")
# 이런 기능을 지원하는 모듈
    print("=== use partial funcion===")
    f = partial(logging, "2017", "12", "28")
    f("python2", "end of support in 2020 ")
    f("python3", "updating")


if __name__ == "__main__":
    main()
