def main():
    x = [1, 2, 3]
    y = {"red": 1, "blue": 2, "green": 3}

    x_iterator = iter(x)
    y_iterator = iter(y)

    print("=== print type ===")
    print(f"list type {type(x)}")
    print(f"dictionary type {type(y)}")
    print(f"list iterator type {type(x_iterator)}")
    print(f"dictionary iterator type {type(y_iterator)}")


    print("=== print next ===")
#StopIteration
    print(f"list iterator next {next(x_iterator)}")
    print(f"list iterator next {next(x_iterator)}")
    print(f"list iterator next {next(x_iterator)}")



if __name__ == "__main__":
    main()
