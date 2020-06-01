def gen(itmes):
    count = 0

    for item in itmes:
        if count == 10:
            return -1

        count += 1
        yield item


if __name__ == "__main__":
    print("=== print gen ===")
    for i in gen(range(15)):
        print(i)
