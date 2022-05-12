laptop = [True, False, True, True, False]
x = any(laptop)
print(x)

cereale = [False, False, False]
x = any(cereale)
print(x)
luna = [True, True, True, False]
d = any(luna)
print(d)

Nume = (f"Numele de familie este adesea cu å")
x = ascii(Nume)
print(x)

x = bin(10)
print(x)  # 0b111000

z = bool(252854)
print(z)
x = bool(56)
print(x)

x = bytearray(1)
print(x)  # x = bytearray(1)

def a():
    x = 56565797131
print(callable(a))

def r():
    x = 2846548

print(callable(r))
s = chr(52)
print(s)
d = chr(97)
print(d)
a = compile('print(100)', 'test', 'eval')
exec(a)
d = complex(25, 52)
print(d)

a = ("Cristina", "X-uleasca", "Y-uleasca")
b = ("Cristulescu", "X-ulescu", "Y-ulescu")

x = zip(a, b)
print(tuple(x))

o = ("Chu-hua ", "Debra", "Mi")
i = ("Ștefan", "Adnan", "Mirko")

a = zip(o, i)
print(tuple(a))


class An:
    luna = "ianuarie"


ziua = "duminica"
ora = 18
a = vars(An)
print(a)


class Person:
    name = "Didi"
    age = 100
    country = "pamant"


x = vars(Person)
print(x)


class An:
    luna = "ianurie"
    ziua = "dumnica"
    ora = "18"


x = vars(An)
print(x)

a = "Soleil", "Terre"
b = 2
c = "Hello world"

x = type(a)
z = type(b)
y = type(c)
print(x)
print(z)
print(y)


class tehnologie:
    laptop = "DELL"
    mobil = "Samsung"
    tableta = "Nexus"


x = vars(tehnologie)
print(x)

s = tuple(("mouse", "claviature", "ecran"))
print(s)

s = str(255153.232)
print(s)

a = int(591515)
print(a)

b = (2, 5, 8, 9, 2)
y = sum(b)
print(y)

v = (2525852, 565641589, 561251321481, 28546131814453215481)
c = sum(v, 2564187415782564145)
print(c)


class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


x = Child("Hello, and welcome!")
x.printmessage()


class Parent:
    def __init__(self, txt):
        self.message = txt

    def printmessage(self):
        print(self.message)


class Child(Parent):
    def __init__(self, txt):
        super().__init__(txt)


x = Child("Hello, and welcome!")
x.printmessage()

a = ("calculator", "laptop", "birou", "chaque", "pas")
x = sorted(a)
print(x)
