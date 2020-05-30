def nested_func():
    def inner_func():
        pass
    p = dir(inner_func())
    print("=== inner attribute ===")
    print(p)


if __name__ == "__main__":
    p = dir(nested_func())
    print("=== attribute ===")
    print(p)
