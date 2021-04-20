import os
import re


def get_name_file(name):
    regex = r"(.+\\)*(.+)\."
    file_path = os.path.abspath(name)
    result = re.findall(regex, file_path)
    print(f'имя файла - {result[0][1]}')
    print(f'путь до файла - {file_path}')


get_name_file('test.txt')
