"""
def print_directory_contents(sPath):
Функция принимает имя каталога и распечатывает его содержимое
в виде «путь и имя файла», а также любые другие
файлы во вложенных каталогах.

Эта функция подобна os.walk. Использовать функцию os.walk
нельзя. Данная задача показывает ваше умение работать с
вложенными структурами.
"""
import os


def print_directory_contents(s_path):
    def dir_files(s_path):
        result = []
        for file_or_dir in os.listdir(s_path):
            full_name = os.path.join(os.path.abspath(s_path), file_or_dir)
            if os.path.isfile(full_name):
                result.append((os.path.abspath(s_path), file_or_dir))
            else:
                result.extend(dir_files(full_name))
        return result
    print(dir_files(s_path))


print_directory_contents('D:\Geekbrains\interview\interview\Lesson1')