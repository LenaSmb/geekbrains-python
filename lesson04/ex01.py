from sys import argv


try:
    _, hours, rate, bonus = argv
except ValueError:
    print('Недостаточно параметров')
    exit(1)


def salary_calc(hours, rate, bonus):
    return hours * rate + bonus

print(f'Размер заработной платы составил: {salary_calc(int(hours), int(rate), int(bonus))}')