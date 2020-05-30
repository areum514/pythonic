ALPHABET_LIST = ['A', 'B', 'C', 'D', 'E', 'F']


def get_index_basic_method():
    i = 0
    for alpbat in ALPHABET_LIST:
        print(f"{i} : {alpbat}")
        i += 1


def get_index_enumerate_method():
    for i, alpbat in enumerate(ALPHABET_LIST):
        print(f"{i} : {alpbat}")


if __name__ == "__main__":
    print("=== get index basic method===")
    get_index_basic_method()

    print("=== get index enumerate method ===")
    get_index_enumerate_method()
