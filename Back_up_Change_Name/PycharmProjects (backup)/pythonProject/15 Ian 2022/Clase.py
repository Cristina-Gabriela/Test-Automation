

class Laptop:
    def __init__(self, price, color, processor):
        self.price = price
        self.color = color
        self.processor = processor

DELL = Laptop(4000, "grey", "i_7")
ACCER = Laptop(3000, "red", "i_5")
HP = Laptop(5000, "metal", "i_7")

print(DELL.price, DELL.color, DELL.processor)
print(ACCER.price, ACCER.color, ACCER.processor)
print(HP.price, HP.color, HP.processor)



class Dog:
    legs = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color


animal = Dog("Fido", "brown")
print(animal.legs)
print(Dog.legs)


class Cars:
    wheel = 4

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def sorum(self):
        print("Vanzare")

    def platforme(self):
        print("Cumparare")

    def sortare_pret(self):
        print("Filtru de pret")

W = Cars("volkswagen", "red")
print(W.wheel)
print(Cars.wheel)
W.sorum()
W.platforme()
W.sortare_pret()




class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color


class Cat(Animal):
    def purr(self):
        print("Purr...")


class Dog(Animal):
    def bark(self):
        print("Woof!")


a = Dog("Fido", "brown")
print(a.color)
a.bark()











