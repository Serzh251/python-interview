
keys = [_ for _ in range(1, 10)]
values = ['first', 'second', 'third', 'fourth', 'fifth']
my_dict = {}

# my_dict.update([el])
# my_dict = {key: [list2] for key in zip(list1)}
# my_dict = dict(zip(list2, list1))
# my_dict.fromkeys(list1[ zip(list2)])
# for value in list2:
#     for key in list1:
#         my_dict.fromkeys(key[value])
# my_dict = my_dict.fromkeys(list1)
my_dict = {key: value for key, value in zip(keys, values)}
print(my_dict)
