a = int(input("Введите первое число a: "))
b = int(input("Введите второе число b: "))


def maxmin(p1, p2):
    if p1 < 0:
        p1 = p1 * -1
    if p2 < 0:
        p2 = p2 * -1
    if p1 > p2:
        maxi = p1
        mini = p2
    else:
        maxi = p2
        mini = p1
    c = maxi - mini
    return c

print(f'''
Сумма a+b: {a + b}
Разность a-b: {a - b}
Произведение a*b: {a * b}
Среднее арифметическое a,b: {(a + b) / 2}
Разность максимального и минимального по модулю a,b: {maxmin(a, b)}''')
