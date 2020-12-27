user_str = input('Введите строку >>> ')

print(1, end=' ')

n = 2

for s in user_str:
    if s == ' ':
        print(s)
        print(n, end=' ')
        n += 1
        continue

    print(s, end='')

print()