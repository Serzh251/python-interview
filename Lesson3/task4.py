import random
import re


def create_file(file_name):
    try:
        with open(file_name, 'x', encoding='utf-8') as f:
            list_numbers = [random.randint(-10, 10) for _ in range(10)]
            # list_letters = [chr(random.randint(64, 90)) for _ in range(10)]
            list_letters = ['example' for _ in range(10)]
            for i, el in enumerate(list_letters):
                list_letters.pop(i)
                list_letters.insert(i, (el + str(random.randint(100, 110))))
            for el in list(zip(list_letters, list_numbers)):
                f.write(str(el) + '\n')
    except FileExistsError:
        print('Файл с таким именем уже существует')
    open_file(file_name)


def open_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        str_data = f.read()
        print(str_data)
        print(f'первое вхождение строки example - {str_data.find("example")}')
        str_example_all = [m.start() for m in re.finditer("example", str_data)]
        print(f'все вхождения строки example - {str_example_all}')
        str_data = re.sub(r'example10', r'simple20', str_data)
        print(f' найденные строки заменены на новые: \n {str_data}')
        print(re.findall(r'\b\w+\b', str_data))



create_file('newfile.txt')