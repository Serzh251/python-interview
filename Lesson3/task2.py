"""Написать программу, которая запрашивает у пользователя ввод числа.
На введенное число она отвечает сообщением, целое оно или дробное.
Если дробное — необходимо далее выполнить сравнение чисел до и после запятой.
Если они совпадают, программа должна возвращать значение True, иначе False."""

import math


def check_number():
    """без обработки ', ' """
    try:
        number = float(input('введите число: '))

    except ValueError:
        print("вы ввели не число, попробуйте снова")
        return

    if number % 1 != 0:
        print('введенное число дробное')
        number_str = str(number)
        number_list = number_str.split('.')
        if number_list[0] == number_list[1]:
            print("число до запятой равно числу после запятой")
            return True
        else:
            print("число до запятой и после нее не равны")
            return False
    else:
        print("введенное число целое")
        return


def check_number_2():
    """обработка с ',' и '.' """
    number = input('введите число: ')

    if len(number.split('.')) > 1:
        number_lst = number.split('.')
    else:
        number_lst = number.split(',')

    if len(number_lst) > 1:
        print('введенное число дробное')
        if number_lst[0] == number_lst[1]:
            print("число до запятой равно числу после запятой")
            return True
        else:
            print("число до запятой и после нее не равны")
            return False
    try:
        number = int(number)
        print('введенное число целое')
    except:
        print('вы ввели не число')


check_number()

check_number_2()
