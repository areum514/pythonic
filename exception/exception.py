EXIST_FILE = "sample_file"
NON_EXIST_FILE = "non_exist_sample_file"

# 예외 처리할 대상과예외발생시 처리하는 코드
# finaly 은 try,except에서 처리하고 난 뒤 반드시 처리해야 할 코드
# python에서는 else 라는 추가 구문 으로 try에서 작성된 코드가 문제없이 실행되면 그 뒤에 실행될 코드를 작성함!
# 기능적으로 try에 작성하는 코드랑 else 에서 작성되는 코드는 차이가 없지만 효율성 측면에서 else가 실행속도가 빠름


def read_file(file_name):
    try:
        f = open(file_name, "r")
    except:
        print("File open error")
    else:
        print(f.read())
        f.close()
    finally:
        print("End file read\n\n")


if __name__ == "__main__":
    print("=== Exist file open ===")
    read_file(EXIST_FILE)

    print("=== Non-Exist file open ===")
    read_file(NON_EXIST_FILE)
