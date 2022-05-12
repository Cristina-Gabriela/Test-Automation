### Python Classes and Objects
# Creați o clasă
#
# Creați obiect
#
# Funcția __init__().
#
# Metode obiect
#
# Parametrul de sine
#
# Modificați proprietățile obiectului
#
# Ștergeți proprietățile obiectului
#
# Ștergeți obiecte
#
# Declarația de trecere

# Python Inheritance
# Creați o clasă pentru părinți
#
# Creați o clasă pentru copii
#
# Adăugați funcția __init__().
#
# Utilizați funcția super().
#
# Adăugați proprietăți
#
# Adăugați metode


### Functii : #### Recapitulare: Functii.
# Apelarea unei funcții

# Argumente  #  o funcție cu un singur argument

# Numărul de argumente

# Argumente arbitrare, *args

# Argumentele cuvintelor cheie

# Argumente de cuvinte cheie arbitrare, **kwargs  # Aici va primi un dictionar

# Valoarea implicită a parametrului  # il suprascrie chiar daca a fost definit la inceput.

# Trecerea unei liste ca argument

# Valori returnate print

# Declarația de trecere


class Jets:

    def __init__(self, name, country):
        self.name = name
        self.origin = country


first_item = Jets("F16", "USA")

a = first_item.name
print(a)

b = first_item.origin
print(b)

c = first_item.name + " " + first_item.origin
print(c)

model = None
country = 0


def __init__(self, name, country):
    self.name = name
    self.origin = country


first_item = Jets("F16", "USA")

a = first_item.name
b = first_item.origin

print(a, b)


class Jets:
    model = None
    country = 0

    def __init__(self, name, country):
        self.name = name
        self.origin = country


first_item = Jets("F14", "USA")
second_item = Jets("SU33", "Russia")

third_item = Jets("AJS37", "Sweden")
fourth_item = Jets("Mirage2000", "France")
fifth_item = Jets("Mig29", "USSR")
sixth_item = Jets("A10", "USA")

first_army = [first_item.name, second_item.name, third_item.name, fourth_item.name, fifth_item.name, sixth_item.name]
print(first_army)


class Jets:
    model = None
    country = 0

    def __init__(self, name, country, quantity):
        self.name = name
        self.origin = country
        self.quantity = quantity


first_item = Jets("F14", "Romania", 87)
second_item = Jets("Mirage2000", "Elvetia", 35)

total = first_item.quantity + second_item.quantity
print(total)


class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner


np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)


class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

    def __str__(self):
        return "{} was the {} in{}".format(self.winner, self.year, self.category)


np2005 = Nobel("Peace", 2005, "Muhammad Yunus")
print(np2005.category, np2005.year, np2005.winner)


class myfunc:
    def fifth(x):
        return x ** 5


ans = myfunc.fifth(5)
print(ans)


class myfunc:
    def fifth(x):
        return x ** 5


ans = myfunc.fifth(5)
print(ans)


class myfunc:
    def power(x, y):
        return x ** y

    def __str__(self):
        return ("My function is something special")


ans1 = myfunc.power(5, 7)
ans2 = myfunc()

print(ans1)
print(ans2)


def function(x, y):
    print(x, y)


function("name", "age")
function("Cris", "30")


# call function with 3 arguments
def func1(x, y, z):
    print(x, y, z)


func1(20, 40, 60)


def func1(*numbers):
    print(*numbers)


def function(*numbers):
    for i in function:
        print(i)


func1(20, 40, 60)
func1(80, 100)


# call function with 2 arguments
def func2(a, b):
    print(a, b)


func2(80, 100)


def func2(*numbers):
    print(*numbers)


func2(20, 40, 60)


def calculation(a, b):
    addition = a + b
    substraction = a - b
    return addition, substraction


res = calculation(40, 10)
print(res)


def outer_fun(a, b):  # 1. la patrat
    square = a ** 2

    def addition(a, b):  # 2. Declaram o alta functie,
        return a + b  # aflam suma returnata

    add = addition(a, b)  # 3. alegem o denumire a unui obiectul din functia din interior si
    return add + 5  # returnam suma + 5


result = outer_fun(10, 30)  # 4. dam valori la functia mare
print(result)  # printam rezultatul


def recursive_function(numbers):
    if numbers:
        return numbers + recursive_function(numbers - 1)
    else:
        return 0


res = recursive_function(10)
print(res)


def display_student(name, age):
    print(name, age)


display_student("Emma", 26)

show_student = display_student
show_student("Vi", 30)

print(list(range(4, 30, 2)))

x = [4, 6, 8, 24, 12, 2]

print(max(x))


class Vehicles:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


x = Vehicle(100, 150)
print(x.max_speed)
print(x.mileage)


class Vehicles:
    pass


class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    class Bus(Vehicle):
        pass


School_bus = Bus("School Volvo", 180, 12)
print("Vehicle Name:",School_bus.name,"Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)


