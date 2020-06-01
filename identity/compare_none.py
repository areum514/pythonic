import timeit


def average(items):
    sum = 0
    for item in items:
        sum += float(item)
    return sum/len(items)


def check_performance(compare_expression, condition):
    results = timeit.Timer(
        compare_expression, setup=condition).repeat(100, 10000)
    return average(results)


def main():
    print("=== compare x is not None ===")
    print(f"identity : {check_performance('x is None', 'x=1')}")
    print(f"equality : {check_performance('x == None', 'x=1')}")

    print("=== compare x is None ===")
    print(f"identity : {check_performance('x is None', 'x=None')}")
    print(f"equality : {check_performance('x == None', 'x=None')}")


if __name__ == "__main__":
    main()
