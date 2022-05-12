"""
string = "dreptunghi"
print(string)

#learning the slicing

print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])
print(string[7])
print(string[8])
print(string[9])


print(string[2:]) #start
print(string[:2])
print(string[:5])  #stop
print(string[5:])
print(string[2:9])
print(string[2:7:2])  # din 2 in 2 step over
print(string[0:-1])
print(string[-1])
print(string[::-1]) # invers
print(len(string)) # length

print(len(string[:-2]))
print(string[1:len(string)]) #from 2 to finish  # adrese pt a vedea daca are un anumit numar de caractere.
print(string.upper())  # convertesc totul in litere mici (in general) sau mari
print(string.find("tu"))  # cere o valoare ca argument
print(string.find("dr"))
string[0] = "f"  # imutability - nu poti sa extragi un anumit element dintr-un string pentru a-l modifica
print(string)


# TO DO : use of the methods for string. (scris cu galben)
#  TO DO : use of the methods for string. (scris cu galben) Primul mesaj sa fie "w" + string ("dreptunghi")
#slicing folosit si sa ajungem sa folosim un dreptunghi : wreptunghi  (scoatem prima pozitie si apoi concatenare.)

"""

string = "inovatii_si_tehnologie"
print(string)

print(string[0])
print(string[1])
print(string[2])
print(string[3])
print(string[4])
print(string[5])
print(string[6])
print(string[7])
print(string[8])
print(string[9])
print(string[10])
print(string[11])
print(string[12])

print(string[2:])

print(string[2:])
print(string[2:10])
print(string[2:7:2])
print(string[-1])
print(string[::-1])
print(len(string[::-1]))
abc = len(string[::-1])

print(abc * "#")
print(abc)
print(string[::-1])
print(string[:: 1])

print(string[:2])
print(string[2:10])



a = "telefon"
print(len(a))
x = len(a) * "*"
print(x)
print(a[::1])
print(a[::-1])

s = len(a[::1])
print(s)
print(s * "*")
v = len(a[:: -1])
print(v)
print(v * "*")
print(a[::-1])
print(a[::1])
print(a[1::])
print(a[2:5])
print(a[::5])
print(a[2:6:2])
print(a[-1:-5:1])

print(len(a[:-2]))
print(a[:-2])
print(a[-2:])
c = a[-2::]
print(c)
d = c[::-1]
print(d)

print(a[1:len(a)])
print(a[0:len(a)])
print(a[2:len(a)])
print(a[3:len(a)])
print(a[4:len(a)])
print(a[5:len(a)])

print(a[0::])
print(a[1::])
print(a[2::])
print(a[3::])
print(a[4::])
print(a[5::])
print(a[6::])
print(a[7::])
print(a[::7])
print(a[::6])
print(a[::5])
print(a[::4])
print(a[::3])
print(a[::2])
print(a[::1])

print(a[:0])
print(a[:1])
print(a[:2])
print(a[:3])
print(a[:4])
print(a[:5])
print(a[:6])
print(a[:7])
print(a[:-1])
print(a[:-2])
print(a[:-3])
print(a[:-4])
print(a[:-5])
print(a[:-6])
print(a[:-7])

b = len(a)
print(b)
j = len(a) * "*"
print(j)

print(j[:0])
print(j[:1])
print(j[:2])
print(j[:3])
print(j[:4])
print(j[:5])
print(j[:6])
print(j[:7])
print(j[:-1])
print(j[:-2])
print(j[:-3])
print(j[:-4])
print(j[:-5])
print(j[:-6])
print(j[:-7])

print(a.upper())
print(a.find("te"))
print(a.find("le"))  # pozitia silabelor
print(a.find("fon"))

print(a.replace("telefon", "mobil"))

a = ["ceas", "mobila", "fereastra", "usa"]
print(a)
b = ["laptop"]
a.extend(b)
print(a)

copac = ["frunze", "pere", "trunchi", "radacina"]
peisaj = ["casa", "bloc"]

copac.extend(peisaj)
print(copac)
x = copac.count("frunze")
print(x)
y = peisaj.count()
print(y)