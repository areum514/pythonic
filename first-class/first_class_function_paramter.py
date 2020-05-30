def squre(x):
    return x*x


def bind(func, arg_list):
    result = []
    for arg in arg_list:
        result.append(func(arg))
    return result


def main():
    arg_list = [5, 10]
    print("Assign variable & send parameter")
    squres = bind(squre, arg_list)
    print(squres)


if __name__ == "__main__":
    main()
