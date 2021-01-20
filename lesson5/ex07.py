import json

def average_profit(firms):
    result = 0
    count = 0

    for profit in firms.values():
        if profit < 0:
            continue

        result += profit
        count += 1

    return result / count

with open('firms.txt') as fd:
    firms = {}

    for line in fd:
        name, firm_type, income, spendings = line.rstrip().split(' ')

        profit = float(income) - float(spendings)

        firms[name] = profit

    result = [firms, {'average_profit': average_profit(firms)}]

with open('firms.json', 'w') as fd:
   json.dump(result, fd)
