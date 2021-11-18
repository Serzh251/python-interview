"""Создать два списка с различным количеством элементов. В первом должны быть записаны ключи, во втором — значения.
Необходимо написать функцию, создающую из данных ключей и значений словарь.
Если ключу не хватает значения, в словаре для него должно сохраняться значение None.
Значения, которым не хватило ключей, необходимо отбросить."""


keys = [_ for _ in range(1, 10)]
values = ['first', 'second', 'third', 'fourth', 'fifth']


my_dict1 = {key: value for key, value in zip(keys, values)}
print(my_dict)

my_dict2 = {}
for i in keys:
    try:
        my_dict2[i] = values[i]
    except:
        my_dict2[i] = None
print(my_dict2)