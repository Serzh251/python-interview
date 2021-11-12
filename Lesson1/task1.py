result_str = (lambda lambda_str: ''.join(lambda_str))


def multiplication_table(x, y):
    """Функция вывода таблицы умножения AxB"""
    a = 1
    b = 1
    result_list = []
    while b <= x:
        while a <= y:
            result_list.append(f'{b} x {a} = {a * b} \t')
            a += 1
        b += 1
        a = 1
    return result_str(result_list)


print(multiplication_table(3, 3))
print(multiplication_table(10, 10))

