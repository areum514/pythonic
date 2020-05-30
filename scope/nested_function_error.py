

def greeting(name):
    greeting_msg = "hello"

# greeting_msg는 전역변수도 지역변수도 아니지.. nonlocal_keyword
    def add_name():
        greeting_msg += " "
        return ("%s%s" % (greeting_msg, name))

    msg = add_name()
    print(msg)


if __name__ == "__main__":
    greeting("python")
