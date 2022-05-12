

# sum simplificat
x = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(sum(x))

# sum: for
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
s = 0
for i in my_list:
    s += i
print(s)

# sum: index
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
s = 0
for i in range(0, len(my_list)):
    s += my_list[i]
print(s)

# sum: while
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
s = 0
x = 0
while x < len(my_list):
    s += my_list[x]
    x += 1
print(my_list)
print(s)

# sum simplificat
list = [10, 235, 2352, 87, 1321, 5164, 2124574, 12, 8]
print(sum(list))

# sum: for
list = [10, 235, 2352, 87, 1321, 5164, 2124574, 12, 8]
s = 0
for i in list:
    s += i
print(s)

# sum: index
list = [10, 235, 2352, 87, 1321, 5164, 2124574, 12, 8]
s = 0
for i in range(0, len(list)):
    s += list[i]
print(s)

# sum: while
list = [10, 235, 2352, 87, 1321, 5164, 2124574, 12, 8]
s = 0
i = 0
while i < len(list):
    s += list[i]
    i += 1
print(s)

# Functions: print and def

x = 12
y = 25
print(x, y)
d = x
x = y
y = d
print(x, y)

salar_gigel = 1232323564654
salar_bibel = 0.12
print(salar_gigel, salar_bibel)

salar_schimbat = salar_gigel
salar_gigel = salar_bibel
salar_bibel = salar_schimbat
print(salar_gigel, salar_bibel)

lista = [5, 56, 12, 5, 54, 1, 56, 122]
rezultat = 0
for i in lista:
    print("Elementele din lista", i)
    print("Rezultatul din lista", rezultat)
    rezultat += i
    break
print(rezultat)

lista = [5, 56, 12, 5, 54, 1, 56, 122]
print(sum(lista))

rezultat = 0
element = 1
while element <= 4:
    rezultat += element
    element += 1
    break
print(rezultat)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
i = 0
for i in lista:
    s += i
print(s)

lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
i = 0
while i < len(lista_2):
    s += lista_2[i]
    i += 1
    break
print(s)

lista_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(lista_3))

lista_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
suma_numerelor = 0
indexarea_numerelor = 0
for i in range(0, len(lista_4)):
    suma_numerelor += lista_4[i]
    indexarea_numerelor += 1
print(suma_numerelor)

lista = [1, 2, 3, 4, 5]
n = 0
i = 0
while i < len(lista):
    i = i - 1
    n += lista[i]
    break
print(n, i)

a = 4
while a < 5:
    a = a + 1
    print(a)
    break


txt = [1, 2, 3, 4, 5]
lungime = len(txt)
for i in range(lungime):
    print(txt[lungime - i - 1])

txt = [1, 2, 3, 4, 5]
txt.reverse()
print(txt)


i = 5
if i > 0 and i < 100:
    print("i has between 0 and 100 years. ")
else:
    print("Error ")

a = int(input("Enter a number"))
if a > 0 and a < 110:
    print("True")
else:
    print("False")

a = 456
b = 456

while a % b == 0:
    if a % b == 0:
        print("True...True")
        break
else:
    print("False")

i = 10
while i > 0:
    i -= 1
    print(i)
    break

i = 100
while i > 0:
    i -= 1
    print(i)
    break

a = ["paine", "mere", "salata", "cirese", "capsuni", "unt", " etc"]
b = ["haine", "casa", "masina", "TGV"]

while a:
    print(a.pop(-1))
    break
print("Finish")

while b:
    print(b.pop(-1))
    break
a = ["paine", "mere", "salata", "cirese", "capsuni", "unt", " etc"]
b = ["haine", "casa", "masina", "TGV"]

v = len(a)
d = len(b)
while v > 0:
    v -= 1
    break
    print(v)
    print(a)

