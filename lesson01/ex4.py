number = int(input("Введите число >>> "))

maxNumber = 0
step = 1

while number > 0:
    result = number // step

    if result > 10:
        step = step * 10
        continue

    number = number % step
    step = 1

    if result > maxNumber:
        maxNumber = result

print(maxNumber)
