LOWER_LIST = ["python", "python2", "python3"]
UPPER_LIST = []

""" 
def convert():
    for data in LOWER_LIST:
        UPPER_LIST.append(data.upper())


def main():
    print("=== print result ===")
    convert()
    print(LOWER_LIST)
    print(UPPER_LIST)
 """

# higher order funcion


def convert(data):
    return data.upper()


def main():
    print("=== print result ===")
    UPPER_LIST = map(convert, LOWER_LIST)
    print(LOWER_LIST)
    print(list(UPPER_LIST))


if __name__ == "__main__":
    main()
