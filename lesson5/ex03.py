def less_than_20k(workers):
    result = []

    for worker in workers:
        if worker['pay'] < 20000:
            result.append(worker)

    return result

def average(workers):
    result = 0
    count = 0

    for worker in workers:
        result += worker['pay']
        count += 1

    return result / count

with open('payroll.txt') as fd:
    workers = []

    for line in fd:
        worker = {}

        name, pay = line.split(' ')

        worker['name'] = name
        worker['pay'] = float(pay.rstrip())

        workers.append(worker)

    print(less_than_20k(workers))
    print(average(workers))