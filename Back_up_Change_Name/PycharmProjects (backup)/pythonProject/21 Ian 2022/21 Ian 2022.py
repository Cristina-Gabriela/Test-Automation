from typing import List, Union

my_tuple = (2, 6565, 121, 121, 212, 12, 21, 7, 89, 9, 40, 4, 7, 8, 9, 1)
print(my_tuple[10])

my_list: List[Union[int, float]] = [10, 20, 3.5, 4.56]
print(my_list)
print(type(my_list))

new_tuple = tuple(my_list)
print(type(new_tuple[:3]))
print(len(new_tuple[:3]))

x, y, *other = (2, 3, 56, 12, 45, 78, 12, 321, 121, 578, 12)
print(other)

last_tuple = 2, 5, 6, 8, 89, 45, 12, 1, 223, 325, 54, 12, 56, 89
print(last_tuple)