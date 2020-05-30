var_shadowing = "global"


def out_function():
    var_shadowing = "outer"

    def inner_function():
        var_shadowing = "inner"
        print(f"inner_function scope {var_shadowing}")
    inner_function()
    print(f"out_function scope {var_shadowing}")


if __name__ == "__main__":
    out_function()
    print(f"global scope {var_shadowing}")
