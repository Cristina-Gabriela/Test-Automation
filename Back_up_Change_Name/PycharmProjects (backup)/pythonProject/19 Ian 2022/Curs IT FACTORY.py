from typing import List, Union

my_tuple = (1, 21, 32, 45, 56, 67, 78, 101, 121)
print(my_tuple[3])

my_list: List[Union[float, int]] = [12.5, 56, 8, 5.2]
print(my_list)
print(type(my_list))

new_tuple = tuple(my_list)
print(type(new_tuple))

print(11 in new_tuple)
print(new_tuple[:3])
print(len(new_tuple[:3]))

x, y, *other = (7, 8, 23, 56, 178, 45, 25, 12)
print(other)  # va da o lista

last_tuple = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
print(last_tuple)    #avantajul tuple -- unele informatii stocate intr-o colectie de date se afiseaza ca date statice. ex. GPS.coordonatele, luni de zile, zile.

#iterarea unui tuple va fi mult mai rapida.
#listele : manipularea datelor va fi foarte mare(flexibilitate,modificate cu usurinta)

#last_tuple.append(7)
#print(last_tuple)   # nu pot fi modificate
#print(list(last_tuple).append(7))













