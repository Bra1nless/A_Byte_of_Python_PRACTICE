def power_sum(power, *args):
    '''Возвращает сумму аргументов, возведенных в указанную степень'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total


print(power_sum(2, 3, 4, 5))
