from typing import List

suma = abs(-12.5)  # returneaza un numar pozitiv, idiferent daca el este poziitv sau negativ.
print(suma)
print(f"Suma de {suma} este primita in euro")
print(f"The sum {suma} is recieved in euro.")

response = [True, True, True]  # Daca toate elementele sunt identitice printeaza acel element. Daca nu, celalalt
x = all(response)
print(x)

my_list: List[str] = ["Ana", "Ana", "Ana", "Ana", "Dan", "Dan"]
y = all(my_list)
print(y)

my_list = ["George", "Ana", "George", "Ana", "George", "Ana", "George", "Ana", "Dan", "George", "Dan", "Dan", "Dan",
           "Dan", "Dan", "Dan", "Dan", "George"]
y = all(my_list)
print(y)

v = ["Cipru, 55.7", "Irlanda, 49.1", "Aruba, 48.4", "Andorra, 45.2", "Islanda, 43.3", "Franța, 42.2",
     "Insula Man, 41.1", "Grecia 41.0", "Danemarca 40.8", "San Marino 38.5"]
print(v)

x = sorted(v)
print(x)

print(len(v))
print(len(v))
print(x[::-1])
print(x[::1])
print(x[1:])

a = ("a", "b", "c", "d")
v = slice(2)
print(a[v])

a = ("a", "b", "c", "d")
v = slice(2, 5)
print(a[v])

a = ("a", "b", "c", "d")
v = slice(0, 5, 2)
print(a[v])

print(type(v))

my_list = [True, True, True, True, True]
y = all(my_list)
print(y)

my_list = [True, True, False, False, False]
y = all(my_list)
print(y)

my_list = [True, False, True, False, True, False]
y = all(my_list)
print(y)

my_list = [False, False, False, False, False]
y = all(my_list)
print(y)

my_lists = [1, 2, 3, 45, 656, 892, 2, 2, 2, 2]
u = all(my_lists)
print(u)

my = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
f = all(my)
print(f)

my = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2]
f = all(my)
print(f)

my = [2, 2, 2, 1, 1, 8, 2, 2, 2, 2]
f = all(my)
print(f)

my_list = [True, True, True, True, False]
y = all(my_list)
print(y)

my_list = [False, False, False, False, True]
w = all(my_list)
print(w)

my_list = [False, False, False, False, False]
y = all(my_list)
print(y)

my_list = [True, True, True, True, True, True]
t = all(my_list)
print(t)

v = ["Cipru", "55.7", "Irlanda", "49.1", "Aruba", "48.4", "Andorra", "45.2", "Islanda", "43.3", "Franța", "42.2",
     "Insula Man", "41.1", "Grecia", "41.0", "Danemarca", "40.8", "San Marino", "38.5"]
print(v)

x = slice(1)
print(v[x])


