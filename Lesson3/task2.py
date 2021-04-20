import math


def check_number():
    number = 0.0
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
            return True
        else:
            return False
    else:
        print("введенное число целое")


if check_number():
    print("число до запятой равно числу после запятой")
else:
    print("число до запятой и после нее не равны")
