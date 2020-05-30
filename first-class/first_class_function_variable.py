def squre(x):
    return x*x


def main():
    print("Function call")
    print(squre(10))

    print("Assign variable")
    f = squre
    print(f(10))


if __name__ == "__main__":
    main()
