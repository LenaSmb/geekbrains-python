with open('test_2.txt') as fd:
    strings = 0

    for line in fd:
        words = 0

        strings += 1

        for ch in line:
            if ch == ' ' or ch == '\n':
                words += 1

        print(f'{words} words in line')

    print(f'Lines - {strings}')