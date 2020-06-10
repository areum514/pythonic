import multiprocessing


def worker(num, num_list):
    p = multiprocessing.current_process()
    print("[%s] num : %s" % (p.name, num.value))
    for idx, value in enumerate(num_list):
        print("[%s] num_list[%s] : %s" % (p.name, idx, value))
    num.value = 50
    for i in range(len(num_list)):
        num_list[i] = num_list[i]*10
        #num_list = [x*10 for x in num_list]


def main():
    single_intager = multiprocessing.Value("i", 5)
    integer_list = multiprocessing.Array("i", range(10))
    p = multiprocessing.Process(
        target=worker, name="worker", args=(single_intager, integer_list))
    p.start()

    p.join()
    print("num : %s" % single_intager.value)

    for idx, value in enumerate(integer_list):
        print("num_list[%s] : %s" % (idx, value))


if __name__ == "__main__":
    main()
