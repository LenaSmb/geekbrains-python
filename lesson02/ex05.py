my_list = [9, 8, 7, 6, 5]

print(f"Рейтинг - {my_list}")

n = 3

while n > 0:
    number = int(input("Введите число >>> "))

    my_list.append(number)
    my_list.sort()
    my_list.reverse()

    print(f"Рейтинг - {my_list}")

    n -= 1
