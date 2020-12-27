user_input = input('Введите элементы списка через пробел >>> ')

l = user_input.split(' ')

list_length = len(l)

for i in range(list_length):
    if i < list_length - 1 and i % 2 == 0:
        l[i], l[i+1] = l[i+1], l[i]

print(l)
