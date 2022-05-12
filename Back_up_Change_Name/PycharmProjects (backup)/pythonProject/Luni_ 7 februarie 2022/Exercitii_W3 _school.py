### Functions ###  Luni

#### Recapitulare: Functii.
# Apelarea unei funcții
def function(type_technology):
    print("This is a new " + type_technology + ".")


function("hyperloop")


# Argumente  #  o funcție cu un singur argument
def function(type_train):
    print("This is the new type of technology: " + type_train + "!")


function("Hyperloop")


# Numărul de argumente
def function(type_technology="quantum computer"):
    print("This is the newest type of technology: " + type_technology)


function(type_technology="quantum computer")


def function(type_technology="quantum computer"):
    print("This is the newest type of technology: " + type_technology)


function(type_technology="5G")
function(type_technology="robotic process automation")
function(type_technology="blockchain")


# Argumente arbitrare, *args
def function(*type_technology):
    print("This is the newest " + type_technology[0] + "!")
    print("This is the newest " + type_technology[1] + "!")
    print("This is the newest " + type_technology[2] + "!")
    print("This is the newest " + type_technology[3] + "!")
    print("This is the newest " + type_technology[4] + "!")


function("hyperloop", "quantum computer", "robotic process automation", "blockchain", "5G")


# Argumentele cuvintelor cheie
def function(type_technology_1, type_technology_2, type_technology_3, type_technology_4, type_technology_5):
    print("This is the newest type of technology: " + type_technology_1)
    print("This is the newest type of technology: " + type_technology_2)
    print("This is the newest type of technology: " + type_technology_3)
    print("This is the newest type of technology: " + type_technology_4)
    print("This is the newest type of technology: " + type_technology_5)


function(type_technology_1="hyperloop", type_technology_2="quantum computer",
         type_technology_3="robotic process automation", type_technology_4="blockchain", type_technology_5="5G")

print(" ")


# Argumente de cuvinte cheie arbitrare, **kwargs  # Aici va primi un dictionar
def function(**type_technology):
    print("This is the newest type of technology 2022: " + type_technology["h"])
    print("This is the newest type of technology 2022: " + type_technology["q"])
    print("This is the newest type of technology 2022: " + type_technology["r"])
    print("This is the newest type of technology 2022: " + type_technology["b"])
    print("This is the newest type of technology 2022: " + type_technology["G"])


function(h="hyperloop", q="quantum computer", r="robotic process automation", b="blockchain", G="5G")


# Valoarea implicită a parametrului  # il suprascrie chiar daca a fost definit la inceput.
def function(type_technology="hyperloop"):
    print("THis is the new trends in 2022: " + type_technology)


function()
function(type_technology="robotic process automation")
function(type_technology="5G")
function(type_technology="quantum computer")
function(type_technology="blockchain")


# Trecerea unei liste ca argument
def function(type_technology):
    for x in type_technology:
        print(x)


new_technology = ["* robotic process automation", "* 5G", "* quantum computer", "* blockchain"]
function(new_technology)

print(" ")


# Valori returnate print
def function(type_technologie):
    return type_technologie * 10


print(function(7))


# Declarația de trecere
def function(type_technology):
    pass


### W3 school ###
# Python Classes and Objects
# Creați o clasă
class Technology:
    inside_class = "inside_class"


print(Technology)


class New_trends_2022:
    inside_news = "the new trends"


print(New_trends_2022)


class Hyperloop:
    train = "New jobs very well paid"


print(Hyperloop)


class Quantum_Computer:
    evolution = "New jobs in one of the famous field"


print(Quantum_Computer)


class Robot_Process_Automation:
    all_around = "Utility and jobs for our present and future"


print(Robot_Process_Automation)

print(" ")


# Creați obiect
class Robot_Process_Automation:
    evolution = "Utility and jobs for all in present and in the future"


print(Robot_Process_Automation)
print(Robot_Process_Automation.evolution)
print("")


class Hyperloop:
    trains = "New jobs and elegance"


mobility = Hyperloop
print(mobility)
print(mobility.trains)
print("")


class New_trends_2022:
    new_jobs = "Hyperloop", "Robot_Process_Automation", "5G", "Quantum Computer", "blockchain"


print(New_trends_2022)
print(New_trends_2022.new_jobs)

print("")


# Funcția __init__().

class Hyperloop:
    def __init__(self, year, color, speed):
        self.year = year
        self.color = color
        self.speed = speed


Hyperloop_Romania = Hyperloop(2024, "green", "1220km/h")

print(Hyperloop)
print(Hyperloop_Romania.year)
print(Hyperloop_Romania.color)
print(Hyperloop_Romania.speed)


class Robot_Process_Automation:
    def __init__(self, robot, color, automation):
        self.robot = robot
        self.color = color
        self.automation = automation


object = Robot_Process_Automation("robot_de bucatarie", "grey", "yes, automation")

print(object.robot)
print(object.color)
print(object.automation)


class Quantum_Computer:
    def __init__(self, name, speed, owner):
        self.name = name
        self.speed = speed
        self.owner = owner


x = Quantum_Computer("Dell", 753, "every person on the planet")
print(x.name)
print(x.speed)
print(x.owner)

print("")


class Blockchain:
    def __init__(self, name, utility, country):
        self.name = name
        self.utility = utility
        self.country = country


x = Blockchain("doctor", "medicine", "Romania")
print(Blockchain)
print(x.name)
print(x.utility)
print(x.country)


# Metode obiect
class Hyperloop:
    def __init__(self, name, year, color, speed):
        self.name = name
        self.year = year
        self.color = color
        self.speed = speed

    def function(self):
        print("Hello, I would like to walk with one " + self.name + ".")


x = Hyperloop("Hyperloop", 2024, "green", "1220km/h")
x.function()


class Quantum_Computer:
    def __init__(self, name, speed, owner):
        self.name = name
        self.speed = speed
        self.owner = owner

    def function(self):
        print("I want to have a " + self.name + ".")


x = Quantum_Computer("Quantum Computer Dell", 753, "every person on the planet")
x.function()
print(x.name)
print(x.speed)
print(x.owner)


class Robot_Process_Automation:
    def __init__(self, robot, color, automation):
        self.robot = robot
        self.color = color
        self.automation = automation

    def function(self):
        print("I really want the newest " + self.robot + ". It will be " + self.color + "." + self.automation)


object = Robot_Process_Automation("Kitchen robot", "grey", "Yes, automation")
object.function()
print(object.robot)
print(object.color)
print(object.automation)


# class automation:
#     def __init__(self, robots, trains):
#         self.robots = robots
#         self.trains = trains
#
#     def function(self):
#         print("The world need automation for developing: " + self.robots + " and " + self.trains + ".")
#
# x = automation("new robots", "new trains")
# x.function()
#
# r1 = automation("all robots")
# r2 = automation("all robots for all the trains")


# Parametrul de sine

# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#
#   def myfunc(self):
#     print("Hello my name is " + self.name +" and I have " + self.age)
#
# p1 = Person("John", "36")
# p2 = Person("Robot", "10")
# p1.age = "40"
# p2.age = "100"
#
# print(p1.age)
# print(p2.age)
# p1.myfunc()
# p2.myfunc()


# Modificați proprietățile obiectului
class blockchain:
    def __init__(self, domain, country):
        self.domain = domain
        self.country = country

    def function(self):
        print("This is a blockchain for the " + self.domain + " in the " + self.country + ".")


x1 = blockchain("medicine", "all world")
x1.function()

x2 = blockchain("technology", "all world")
x2.function()


# Ștergeți proprietățile obiectului
# del x1.age
# print(x1.age)

# Ștergeți obiecte
# del x2.age
# print(x2.age)

# Declarația de trecere
class Technology:
    pass


class Blockchain:
    pass


class Robot_Process_Automation:
    pass


class Quantum_Computer:
    pass


class Hyperloop:
    pass


# Create Object
class medicine:
    x = "automation"


medicine()


# The __init__() Function

class medicine:
    def __init__(self, domain, country):
        self.domain = domain
        self.country = country


x = medicine(" - internal", " - around the world")
print(x.domain)
print(x.country)


class industry:
    def __init__(self, musical, technology, medicine, tourism):
        self.musical = musical
        self.technology = technology
        self.medicine = medicine
        self.tourism = tourism


x = industry("artists", "Automation", "blockchain", "infrastructure")
print(industry)
print(x.musical)
print(x.technology)
print(x.medicine)
print(x.tourism)

y = industry("musical", "technology", "medicine", "tourism")
print(industry)
print(y.musical)
print(y.technology)
print(y.medicine)
print(y.tourism)


# Object Methods
class industry:
    def __init__(self, musical, technology, medicine, tourism):
        self.musical = musical
        self.technology = technology
        self.medicine = medicine
        self.tourism = tourism

    def function(self):
        print(
            "This is un update of news on industry in: " + self.medicine + "," + self.technology + "," + self.tourism + "," + self.musical)


x = industry("blockchain_in_medicine", "blockchain_in_technology", "blockchain_in_tourism", "blockchain_in_music")
x.function()


# The self Parameter
class industry:
    def __init__(abc, musical, technology, medicine, tourism):
        abc.musical = musical
        abc.technology = technology
        abc.medicine = medicine
        abc.tourism = tourism

    def function(abc):
        print(
            "This is un update of news on industry in: " + abc.medicine + "," + abc.technology + "," + abc.tourism + "," + abc.musical)


x = industry("blockchain_in_medicine", "blockchain_in_technology", "blockchain_in_tourism", "blockchain_in_music")
x.function()


# Modify Object Properties
class technology:
    def __init__(self, blockchain, automation, hyperloop):
        self.blockchain = blockchain
        self.automation = automation
        self.hyperloop = hyperloop

    def function(self):
        print("This is the new technology: " + self.blockchain + self.automation + self.hyperloop)
x1 = technology("tech", "auto","speed")
x1.blockchain = "tech"
print(x1.blockchain)
print(x1.automation)
print(x1.hyperloop)
print(technology)









# Delete Object Properties
# Delete Objects
# The pass Statement


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


### udemy ###
# Python Classes and Objects
# Python Inheritance

## Pauza
### Tema :
# https://holypython.com/advanced-python-exercises/exercise-4-classes/
# https://pynative.com/python-functions-exercise-with-solutions/

#### To Sum up: classes and objects, inheritance

# Ex. Functii udemy.

### W3 school ###
# Python Iterators
# Python Scope
# Python Modules
# Python Datetime
# Python Math
# Python JSON
# Python RegEx
# Python PIP
# Python Try Except
# Python User Input
# Python String Formatting

# Python Iterators
# Python Scope
# Python Modules
# Python Datetime
# Python Math
# Python JSON
# Python RegEx
# Python PIP
# Python Try Except
# Python User Input
# Python String Formatting

### Kylie Ying
# Using Functions in Python
# Using Classes and Objects in Python
# Inheritance/Polymorphism in Object Oriented Programming | Python for Beginners | Code with Kylie #10


# Enjoy : Code https://www.w3schools.com/codegame/index.html
