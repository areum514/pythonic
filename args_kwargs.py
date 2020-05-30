def args_test(*args):
    print("=== args list ===")
    for arg in args:
        print(f"Argument {arg}")


def kwargs_test(**kwargs):
    print("=== kwargs list ===")
    for keyword, arg in kwargs.items():
        print(f"Argument {keyword}, arg {arg}")


def main():
    args = ["red", "blue"]
    kwargs = {"red": "color", "blue": "color"}
    args_test(*args)
    kwargs_test(**kwargs)


if __name__ == "__main__":
    main()

# args = arguments  non-keyworded 가변인자 다루고
# kwargs = keyword arguments keyworded 가변인자 다루고
