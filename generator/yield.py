def gen():
    value = 1
    while True:
        value = yield value #yield로 값을 반환하는 동시에 할당 


def main():
    print("=== print gen function ===")
    g = gen()

    print(next(g))
    print(g.send(2))
    print(g.send(10))
    print(g.send(5))
    print(next(g))


if __name__ == "__main__":
    main()
