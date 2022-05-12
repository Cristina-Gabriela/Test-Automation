
a = "23484154"
print(a.isdecimal())

b = "fijerifge4145"
print(b.isdecimal())

s = "15414515"
if s.isdecimal() == True:
    print("Acesta este un enunt pozitiv")
else:
    print("Nu este un enunt pozitiv")

a = "Ciocolata"
print(a.isdecimal())
b = "15454845481"
print(b.isdecimal())

s = "18545848548"
if s.isdecimal() == True:
    print("Acesta este un isdecimal")
else:
    print("Acesta nu este un isdecimal")

a = 'fvbgbufic281841'
print(a.isidentifier())

b = 'nufvufdaakmkaki'
print(b.isidentifier())

c = '8451 vfrbgr 4874 vfvgfr'
print(c.isidentifier())

s = "jnjnjnn54545cjfdjv584vd18vf4d"
if s.isidentifier() == True:
    print("E ok daca nu exista spatii")
else:
    print("Nu e ok daca nu exista spatii")

a = "vmivcsoj"
print(a.islower())

b = "ckjhfdANJKHHDFJVDBBufndfvsdcnvidb"
print(b.islower())

a = "nchfenjnjnkndsllsk25656"
if a.islower() == True:
    print("litere mici cu islower")
else:
    print("litere mici, mari sau doar mari")

a = "52865451484541851"
print(a.isnumeric())

b = "#$#fvfdsuvf12#@#"
print(b.isnumeric())

c= "5256481841"
print(c.isnumeric())

a = "mfudihfeh2863154"
if a.isnumeric() == False:
    print("Este corect,isnumeric nu este in a ")
else:
    print("A contine doar numere ")

a = 'ncbudvbfeu'
print(a)
print(a.isprintable())

b = "cvmdfvd258645vrdgf1@#$%^&*()(%$#@!"
print(b)
print(b.isprintable())

d = "jfbebfjbdcjb2564514dscds565765d%$$%"
if d.isprintable() == True:
    print("True")
else:
    print("Not True")

t = chr(2) + chr(10)
if t.isprintable() == True:
    print("Printeaza")
else:
    print("Eroare")

s = "2 + 4 + 4 + 5"
if s.isprintable() == True:
    print("Printeaza")
else:
    print("Eroare")

s = "ndjvufdufd"
print(s.isspace())

v = " \t \t \t\t"
print(v.isspace())

g = "\n"
print(g.isspace())

k = "\t \t \t"
if k.isspace() == True:
    print("True")
else:
    print("False")

a = "IT"
print(a.istitle())

n = 'Python Is Good !'
print(n.istitle())

f = 'Este Soare'
if f.istitle() == True:
    print("Este soare afara")
else:
    print("Norii nu s-au imprastiat")
a = "Ce gandesti?"
print(a.isupper())

b = "CE GANDESTI?"
print(b.isupper())

a = "CE GANDESTI"
if a.isupper() == True:
    print("GANDESTI OK")
else:
    print("nu gandesti ok")

a = ["Dezvoltare: ", "umana, ", "teritoriala, ", "IT, ", "etc. "]
print("".join(a))

Abc = "2348fjhbhb"
print("Abc:", Abc)

Tehnologie = "mfdvighuh52654"
print("Tehnologie:", Tehnologie)

d = 23
g = 52
x = "d" + "151" + "b" + "cnjus"
print("g.join(d):", x)
print("d.join(g):", x)

x = {"1", "2", "3", "4"}
s = ", "
print(s.join(x))

z = {"Ora", "de", "IT"}
a = "__>__>__>"
print(a.join(z))

v = {"Ora", "de", "it"}
l = "---"
print(l.join(v))


a = "dog"
width = 200
print(a.ljust(width))

a = "dog"
width = 10
fillchar = "*"
print(a.ljust(width, fillchar))

jkj = "nfrughru"
width = 20
fillchar = "#"
print(jkj.ljust(width, fillchar))

a = "jnjnj"
width = 20
fillchar = "*"
print(a.rjust(width, fillchar))

a = "IT, TEHNOLOGIE, INOVATIE,CLUSTERE"
print(a.lower())

n = "it, tehnologie, inovatie, clustere"
d = "it, tehnologie, inovatie, clustere"
if n.lower() == d.lower():
    print('it, tehnologie, inovatie, clustere')
else:
    print("nimic ok")


d = "IT, TEHNOLOGIE, INOVATIE, CLUSTERE"
f = "IT, TEHNOLOGIE, INOVATIE, CLUSTERE"
h = "IT, TEHNOLOGIE, INOVATIE, CLUSTERE"
print(h.lower())

if d.upper() == f.upper():
    print("IT, TEHNOLOGIE, INOVATIE, CLUSTERE")
else:
    print("Not ok")

d = "tehnologie"
print(d.upper())

i = "it, tehnologie, inovatie, clustere"
v = "it, tehnologie, inovatie, clustere"
print(i.upper())
print(v.upper())
if i.upper() == v.upper():
    print("Scrisul va fi in Majuscule")
else:
    print("Scrisul va fi in minuscule")

a = "Tehnologie, inovatie si clustere"
print(a.swapcase())
b = "CLUSTERE, INOVATIE SI TEHNOLOGIE"
print(b.swapcase())

if a.swapcase() != b.swapcase():
    print("Textul este asemanator")
else:
    print("Swapcase nu a functionat")

a = "    tehnologie     *****"
print(a.lstrip())
print(a.lstrip("gie"))
print(a.lstrip("teh"))

f = "inovatie      *****"
print(f.rstrip())
print(f.rstrip("ie"))

d = "      mvifdhggh            "
print(d.strip())

a = "Voi rade iar si voi da farmec visarilor "
print(a.partition("si"))
print(a.partition("rade"))
print(a.partition("visarilor"))

stare = {"a": "564", "b": "898", "d": "2415"}
dictionare = "abd"
print(dictionare.maketrans(stare))
print(stare)

primul = "abc"
al_doilea = "def"
al_treilea = "abc"
print(al_treilea.maketrans(primul, al_doilea))

a = "Voi rade iar si voi da farmec visarilor "
print(a.rpartition("si"))
print(a.rpartition("rade"))
print(a.rpartition("visarilor"))


primul_element = "abc"
al_doilea_element = "ghi"
al_treilea_element = "ab"

string = "abcdefghi"
print("Original string:", string)

translation = string.maketrans(primul_element,al_doilea_element, al_treilea_element)
print("Translated string:", string.translate(translation))



