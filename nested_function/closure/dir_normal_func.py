def normal_func():
    pass


if __name__ == "__main__":
    p = dir(normal_func())
    print("=== attribute ===")
    print(p)
