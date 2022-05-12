
list = []
for i in range(1500, 2700):
    if (i % 7 == 0) and (i % 5 == 0):
        list.append(str(i))
print(",".join(list))

my_list2 = [19, 19, 15, 5, 3, 5, 5, 2]
x = 0
a = 0
while x >= 19 and a >= 5:
    if x >= 19 and a >= 5:
        print("True")
        print([19, 19, 5, 5, 5])
    else:
        print("Not True")
print("Finish")

my_list2 = [19, 19, 15, 5, 3, 5, 5, 2]
x = 0
y = 0
for x in my_list2:
    if x == 2:
        print("True")
        break
for y in my_list2:
    if y == 5:
        print("True again")
        break
print("Finish")

my_list2 = [19, 19, 15, 5, 3, 5, 5, 2]
x = 0
a = 0
while x and a in [19, 19, 15, 5, 3, 5, 5, 2]:
    if x >= 20 and a >= 6:
        print("True")
        print([19, 19, 5, 5, 5])
    else:
        print("Not True")
print("Finish")

my_list3 = [19, 19, 15, 5, 3, 5, 5, 2]

def test(my_list3):
    return my_list3.count(19) == 2 and my_list3(5) >= 3

from typing import List

lista: List[int] = [19, 19, 15, 5, 5, 5, 1, 2]
print(type(lista))
print(len(lista))
print(lista[5])

if len(lista) == 8:
    print("True")
else:
    print("False")

if lista.count(5) == 3:
    print("True")
else:
    print("False")

# 1. Write a Python program to sum all the items in a list.
from typing import List

list = [1, 2, 3, 4, 5, 6]
print(sum(list))

list = [1, 2, 3, 4, 5, 6]
i = 0
s = 0
for i in list:
    s += i
    i += 1
print(list)
print(s)

# 2. Write a Python program to multiply all the items in a list.
list = [2, 3, 4, 5, 6, 5, 78, 45]
print(list * 2)

# 3. Write a Python program to get the largest number from a list
list = [10, 20, 30, 45, 56, 10, 20]
print(max(list))

# 4. Write a Python program to get the smallest number from a list
list = [10, 20, 30, 45, 56, 10, 20]
print(min(list))

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings
# Sample_list: List[str] = ['abc', 'xyz', 'aba', '1221']
# print(len(Sample_list))
# --------------

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# f = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# print(f.sort)

# 7. Write a Python program to remove duplicates from a list.
# list_1 = ["a", "b", "a", "c", "c"]
# a = list_1(dict.fromkeys(list_1))
# print(a)

# 8. Write a Python program to check if a list is empty or not
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(len(a))
b = []
print(len(b))
if not b:
    print("This is an empty list")
s = []
if not s:
    print("This list is empty")

# 9. Write a Python program to clone or copy a list.
a = [25, 56, 12, 45, 12, 45, 4]
b = a.copy()
print(b)
print(a, b)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words
# 11. Write a Python function that takes two lists and returns True if they have at least one common member.
from typing import List
a = {"abc", "bhn","jdl","ais"}
b = {"abc", "ais","dniodh", "disf","djis","djl"}
print(a.intersection(b))

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
a = ["Rosu", "Verde", "Alb", "Negru", "Roz", "Galben"]
# Verde, Alb,Negru - ramas

b = a[0] + " " + a[4] + " " + a[5]
print(b)

i = 0
for i in a:
    if i not in (0, 4, 5):
        print("Verde", "Alb", "Negru")

n = 0
for n in a:
    print(n)

d = (a[1] + " " + a[2] + " " + a[3])
v = (a[0] + " " + a[4] + " " + a[5])
print(d)
print(v)

#13. Write a Python program to generate a 3*4*6 3D array whose each element is *
shape = [[ ["IT" for col in range(10)] for col in range (4)] for row in range (3)]
shape_1 = [[ ["Automation" for col in range(10)] for col in range (4)] for row in range (3)]
shape_2 = [[ ["Technology" for col in range(10)] for col in range (4)] for row in range (3)]
shape_3 = [[ ["Success" for col in range(20)] for col in range (4)] for row in range (3)]
shape_4 = [[ ["Good" for col in range(10)] for col in range (4)] for row in range (3)]
print(shape)
print(shape_1)
print(shape_2)
print(shape_3)
print(shape_4)
print(shape)
print(shape_1)
print(shape_2)
print(shape_3)
print(shape_4)
print(shape)
print(shape_1)
print(shape_2)
print(shape_3)
print(shape_4)
print(shape)
print(shape_1)
print(shape_2)
print(shape_3)
print(shape_4)


# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

a = [11, 12, 13, 14, 15, 16, 17, 18, 19, 121, 23, 25, 21, 20, 20, 26, 89, 90, 100]
if a % 2 == 0:
    print(a)
for x in a:
    if x%2 !=0:
        print(a)

# 15. Write a Python program to shuffle and print a specified list.
from random import shuffle
a = [10,12,15,14,18,19,20]
shuffle(a)
print(a)

from random import shuffle
lista = [10,25,2,7,89,56,4,2,1,2,6,2,7,8,12,58,45]
shuffle(lista)
print(lista)

# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)

#primele si ultimele 5
#valorile sunt patrate ale numerelor 1 - 30

lst = list(range(1,30+1))
print(lst)
print(lst[:5])
print(lst[-5:])

lst = [i*i for i in range(1,30+1)]
print(lst)
print(lst[:5])
print(lst[-5:])

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

new_list = [i * i for i in range(1, 30 + 1)]
print(new_list)
print(new_list[5:])

# 18. Write a Python program to generate all permutations of a list in Python.

from itertools import permutations

l = list(permutations(range(1, 4)))
print(l)

from itertools import permutations

lista_mea = list(permutations(range(1, 3)))
print(lista_mea)

# 19. Write a Python program to get the difference between the two lists
# a = [1, 2, 3, 4, 5, 6]
# b = [2, 5, 6, 7, 8, 9, 10, 23, 4]

# 20. Write a Python program access the index of a list.
a = [1, 5,89,12, 80, 19]
i = 0

for i,x in enumerate(a):
    print(x,i)
"""
# Python Dictionary [ 80 exercises with solution]
# 1. Write a Python script to sort (ascending and descending) a dictionary by value
a = {145, 2, 653, 465, 55, 65, 75, 48, 91, }
print(sorted(a))

"""