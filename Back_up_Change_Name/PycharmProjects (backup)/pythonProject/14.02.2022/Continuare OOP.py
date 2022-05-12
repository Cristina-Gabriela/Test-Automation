# # #
# # # # INHERITANCE
# # # class Flower():
# # #     def __init__(self):
# # #         print("Flower created !")
# # #     def creste(self):
# # #         print("Floarea creste ")
# # #     def infloreste(self):
# # #         print("Floarea infloreste !")
# # #
# # # class Orhidee(Flower):
# # #     def __init__(self):
# # #         Flower.__init__(self)
# # #         print("Orhidee created")
# # #     def isi_schimba_culoarea(self):
# # #         print("Orhideea isi schimba culoarea")
# # #     def rezista_in_timp(self):
# # #         print("Orhideea rezista in timp")
# # #
# # # instanta = Flower()
# # # instanta.creste()
# # # instanta.__init__()
# # # instanta.infloreste()
# # # print("")
# # # variabila = Flower()
# # # variabila.creste()
# # # variabila.infloreste()
# # # print("")
# # # instanta = Orhidee()
# # # instanta.creste()
# # # instanta.infloreste()
# # #
# # # print("")
# # # floricica_mea = Orhidee()
# # # floricica_mea.creste()
# # # floricica_mea.infloreste()
# # # floricica_mea.rezista_in_timp()
# # # floricica_mea.isi_schimba_culoarea()
# #
# # # POLYMORHISM
# #
# # class Flower:
# #     def __init__(self, name):
# #         self.name = name
# #     def infloreste(self):
# #         return self.name + "infloreste !"
# #
# # class Copac:
# #     def __init__(self, name):
# #         self.name = name
# #     def infloreste(self):
# #        return self.name + "infloreste !"
# #
# #
# # floarea = Flower("Orhideea ")
# # copacul = Copac("Ciresul ")
# # print(floarea.infloreste())
# # print(copacul.infloreste())
# # print("")
# # for vegetatie in [floarea, copacul]:
# #     print(type(vegetatie))
# #     print(type(vegetatie.infloreste()))
# #     print(vegetatie.infloreste())
# # print("")
# #
# #
# # def vegetatie_infloreste(vegetatie):
# #     print(vegetatie.infloreste())
# # vegetatie_infloreste(floarea)
# # vegetatie_infloreste(copacul)
# #
# # print("")
# # def x (y):
# #     print(y.infloreste())
# # x(floarea)
# # x(copacul)
# # print("")
# # def x (y):
# #     print(floarea.infloreste())
# #     print(copacul.infloreste())
# #
# # print(" ")
# # print(" ")
# # class Vegetatie:
# #     def __init__(self, name):
# #         self.name = name
# #
# # class Flower(Vegetatie):
# #     def iese (self):
# #         return self.name + "iese!"
# #
# # class Copac(Vegetatie):
# #     def inmugureste(self):
# #        return self.name + "inmugureste !"
# #
# #
# # natura1 = Flower("Ghiocelul ")
# # print(natura1.iese())
# # natura2 = Copac('Marul ')
# # print(natura2.inmugureste())
#
#
# class Bani:
#     def __init__(self, name, job):
#         self.name = name  # variabila de instanta unica pentru fiecare instanta
#         self.job = job
#
#
# class Venituri(Bani):
#     def care_intra(self):
#         # print(self.name + "care se transforma in venituri")
#         print(self.job + " care face ca " + self.name + " sa se transforme in venituri.")
#
#
# class Cheltuieli(Bani):
#     def care_ies(self):
#         print(self.name + "care se transforma in cheltuieli, in ciuda unui " + self.job + ".")
#
#
# x = Bani("euro", "job")
# a = Venituri("50000 euro ", "Jobul")
# a.care_intra()
# b = Cheltuieli("10000 euro ", "job")
# b.care_ies()
#
# print("")
# # POLYMORHISM
#
# for ceva in [a]:
#     ceva.care_intra()
#
# for ceva in [b]:
#     ceva.care_ies()
#
# print(" ")
# # x = Bani
# # a = Venituri
# # b = Cheltuieli
#
# def ceva(x):
#     print(x.care_intra())
#
# a.care_intra()
# b.care_ies()

# # ceva(a)
# # ceva(b)


# Special, Dunder Methods :OOP

# __init__ :
# __str__  : tine loc de print.
# __del__  : sterge clasa.

# class Vacanta:
#     def __init__(self, title, passengers, budget):
#         self.title = title
#         self.passengers = passengers
#         self.budget = budget
#
#     def __str__(self):
#         return f"Aceasta este vacanta cu titlul: {self.title}, cu un numar de pasageri : {self.passengers}"
#
#     def __len__(self):
#         return self.budget
#     def __del__(self):
#         print("Holiday has been deleted !")
#
# created_instance = Vacanta("La munte", "50",5000)
# print(created_instance)   # what is string representation of created instance.
# print("")
# str(created_instance) # it makes the same thing like print
# print(created_instance.budget)
# print(created_instance)
# len(created_instance)
# del created_instance


# def sqrt(param):
#     pass
#
#
class Line:

    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1, y1 = self.coor1
        x2, y2 = self.coor2
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self, x1=3, x2=8, y1=2, y2=10):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.x2 = x2

        print((y2 - y1) / (x2 - x1))


coordinate1 = (3, 2)
coordinate2 = (8, 10)

li = Line(coordinate1, coordinate2)
li.distance()

# 9.433981132056603
#
li.slope()
#
# 1.6

#
print('')

import math

print(math.pi)


class Cylinder:

    def __init__(self, height=2, radius=3):
        self.height = height
        self.radius = radius

    def volume(self, radius=3, height=2, pi=3.14):
        print(pi * radius ** 2 * height)

    def surface_area(self, pi=3.14):
        print(2 * pi * self.radius * self.height + 2 * pi * self.radius ** 2)
        #  2π r h + 2π r²


# 3,14×3²×2
# 2×3,14×3×2+2×3,14×3²

# EXAMPLE OUTPUT
c = Cylinder(2, 3)

c.volume()

# 56.52

c.surface_area()

# 94.2


class Bank_Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amount):
        self.balance = self.balance + dep_amount
        print(f"Dear " + self.owner + ",In your account has been added" + dep_amount)
    def withdrawl(self, wd_amount):
        if self.balance >= wd_amount:
            self.balance = self.balance - wd_amount
            print("The sum accepted")
        else:
            print("The sum depass your budget!")
    def __str__(self):
        return f"Owner: {self.owner} \nBalance: {self.balance}"

i = Bank_Account("Person", 100000)
print(Bank_Account)
print(i.owner)
print(i.balance)
print(i.deposit)












