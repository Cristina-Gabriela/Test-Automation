x = 220
y = 235
print("y") if x >y else print("x") if x< y else print("xy")

o = 56
v = 89
print("o") if o < v else print("v") if o > v else print("ov")

d = 100
f = 102
print("d") if d<f else print("f") if f<d else print("df")

d = 100
f = 102
print("d") if d<f else print("f") if f<d else print("df")

x = 10
y = 23
s = 10
if x < y and x == s:
    print("Toate sunt corecte")

x = 12
y = 56
u = 12
if x > y  or x == u:
	print("Corect !")

a = 12

if a > 2:
    print("Corect!")
    if a > 5:
        print("Corect!")
        if a > 10:
            print("Corect!")
            if a < 50:
                print("Corect!")
                if a < 500:
                    print("Iar corect!")
    else:
        print("Nu se poate!")

x = 10
y = 12
z = 10
if x == z and x < 12:
   print("Finish")

a = 1
while a < 6:
  print(a)
  a += 1

# Simple Definite Loop:
for i in [5, 4, 3, 2, 1]:
    print(i)
print("Finish")

# A Definite Loop with String:
friends = ["A", "B", "C", "D", "E", "F"]
for i in friends:
    print("Happy new year: ", i)
print("Finish")

# the biggest number :
x = 0
print('Start', x)
for i in [2, 5, 6, 8, 4, 6, 2]:
    if i > x:
        x = i
        print(x, i)
print("The biggest number", x)

# Count :
x = 0
print("Incepem acum", x)
for i in [10, 25, 65, 23, 101, 2]:
    x = x + 1
    print(x, i)
print("Numaram pana la :", x)

# Sum :
count = 0
sum = 0
print("Before", count, sum)
for value in [7, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print("Numarare, suma, suma impartia la numarul de caractere: ", count, sum, sum / count)

a = 0
b = 0
print("Incepem de la :", a, b)
for i in [2, 3, 4, 5, 6]:
    a = a + 1
    b = b + i
    print(a, b, i)
print("Final, nr. de caractere, suma, suma impartita la nr. de caractere.", a, b, b / a)

# Filter in a Loop:
print("Inainte")
for i in [1, 2, 3, 4, 45, 46, 27, 28, 9, 20]:
    if i > 20:
        print("Numar mai mare ca 20: ", i)
print("Finish")

# Search Using a Boolean Variable : _ dar fals ca logica intr-un sir cronologic
found = False
print("PLecam de la premiza ca e: ", found)
for i in [1, 2, 3, 4, 5, 12, 56, 56, 7, 1211, 233, 2112, 78]:
    if i > 56:
        found = True
    print(found, i)
print("Finish", found)


found = False
print("Verificam care e adevarata si care e falsa",found)
for i in [2,5,6,64,12,78,212,23,24,56,78,21,1]:
    if i == 64:
        found = True
    print(found,i)
print("Finish",found )

# nu afiseaza nimic, folosim pass pentru a evita o eroare.
a = 33
b = 200

if b > a:
  pass

for a in "bucurie":  # bucurie pe verticala, fiecare litera.
	print(a)











