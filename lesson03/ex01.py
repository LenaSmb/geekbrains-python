a = int(input('Введите 1-ое число >>> '))
b = int(input('Введите 2-ое число >>> '))

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError

    return a / b
