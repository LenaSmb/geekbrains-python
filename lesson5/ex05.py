New_file = 'test_3.txt'

Numb = '13 67.2 23 105.5 33 0 4815.1'

summ = 0

try:
    with open(New_file, 'w') as fhs:
        fhs.write(Numb)

    with open(New_file, 'r') as fhd:
        data = fhd.read()

    for item in data.split():
        summ += float(item)
except IOError as e:
    print(e)
except ValueError:
    print('Некорректные данные')

print(summ)
