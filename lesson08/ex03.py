class NotNumberError(Exception):
    pass

numbers = []

while True:
    data = input('Введите число >>> ')

    if data == 'stop':
        print(numbers)
        break

    try:
        if data.isdigit():
            numbers.append(int(data))
        else:
            raise NotNumberError
    except NotNumberError:
        print(f'{data} - не является числом')


