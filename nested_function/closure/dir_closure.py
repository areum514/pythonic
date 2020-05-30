def closure():
    def inner():
        pass

    p = dir(inner())
    print("=== inner attribute ===")
    print(p)
    return inner


if __name__ == "__main__":
    p = dir(closure())
    print("=== attribute ===")
    print(p)
    # nonlocal변수를 사용하지 않아 none으로 출력됨!
    print(closure().__closure__)
