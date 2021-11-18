""" Написать программу, которая будет содержать функцию для получения имени файла из полного пути до него.
При вызове функции в качестве аргумента должно передаваться имя файла с расширением.
В функции необходимо реализовать поиск полного пути по имени файла,
а затем «выделение» из этого пути имени файла (без расширения)."""

import os
import re


def get_name_file(name):
    regex = r"(.+\\)*(.+)\."
    file_path = os.path.abspath(name)
    result = re.findall(regex, file_path)
    print(f'имя файла - {result[0][1]}')
    print(f'путь до файла - {file_path}')


get_name_file('test.txt')
