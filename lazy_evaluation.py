import time


def wait_return(num):
    print("sleep")
    time.sleep(0.5)
    return num


def print_item(items):
    for i in items:
        print(i)


def main():
    print("=== print list comprehension ===")
    iterator_list = [wait_return(i) for i in range(10)]
    print_item(iterator_list)

    print("=== print generator expression ===")
    iterator_list = (wait_return(i) for i in range(10))
    print_item(iterator_list)


if __name__ == "__main__":
    main()
