with open('test_1.txt', 'w') as fd:
    while True:
        line = input('Введите строку: ')

        if line == '':
            exit()

        fd.write(line + '\n')
