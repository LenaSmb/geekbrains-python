def my_func_1(x, y):
    return 1 / x ** abs(y)

def my_func_2(x, y):
    power = 1

    for _ in range(abs(y)):
        power *= x

    return 1 / power
