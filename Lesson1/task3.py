"""Разработать генератор случайных чисел.
В функцию передавать начальное и конечное число генерации (нуль необходимо исключить).
Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону: “elem_<номер_элемента>”.
Вывести содержимое созданных списка и словаря."""
import random


def gen_random_number(start, stop):
    result_list = []
    result_dict = {}
    for i in range(100):

        random_numder = random.randint(start, stop)
        while random_numder == 0:
            random_numder = random.randint(start, stop)
        result_list.append(random_numder)
        result_dict.update({f'elem_{i}': random_numder})

    print(result_dict)
    print(result_list)


gen_random_number(-5, 5)
