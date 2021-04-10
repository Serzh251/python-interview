def multiplication_table(x, y):
    """Функция вывода таблицы умножения AxB"""
    a = 1
    b = 1
    while b <= x:
        while a <= y:
            print(f'{b} x {a} = {a * b}')
            a += 1
        b += 1
        a = 1


multiplication_table(3, 3)
multiplication_table(10, 10)