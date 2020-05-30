def closure():
    x = 10
    y = 20

    def inner():
        z = 30
        return x+y+z

    p = dir(inner())
    print("=== inner attribute ===")
    print(p)
    return inner


if __name__ == "__main__":
    p = closure()
    print("=== attribute closure ===")
    print(len(p.__closure__))
    print(dir(p.__closure__[0]))
    print(p.__closure__[0].cell_contents)
    print(p.__closure__[1].cell_contents)
