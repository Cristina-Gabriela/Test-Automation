# # polimorphism
#
# class Floare:
#     def intro(self):
#         print("Introducere")
#
#     def cuprins(self):
#         print("Cuprins")
#
#     def incheiere(self):
#         print("Incheiere")
#
#
# class Floricica(Floare):
#     def cuprins(self):
#         print("Cuprins F.")
#
#
# class Verde(Floare):
#     def incheiere(self):
#         print("Incheiere V.")
#
#
# x = Floare()
# y = Floricica()
# z = Verde()
#
# x.intro()
# x.cuprins()
# x.incheiere()
#
# y.intro()
# y.cuprins()
# y.incheiere()
#
# z.intro()
# z.cuprins()
# z.incheiere()


#
# class Floare:
#     def intro(self):
#         print("Introducere")
#
#     def cuprins(self):
#         print("Cuprins")
#
#     def incheiere(self):
#         print("Incheiere")
#
#
# class Floricica(Floare):
#     def creste(self):
#         print("Creste F.")
#
#
# class Verde(Floare):
#     def inverzeste(self):
#         print("Invererste V.")
#
#
# x = Floare()
# y = Floricica()
# z = Verde()
#
# x.cuprins()
# x.incheiere()
# x.intro()
#
# y.cuprins()
# y.intro()
# y.incheiere()
# y.creste()
#
# z.inverzeste()
# z.incheiere()
# z.intro()
# z.cuprins()
# from self import self

# class Floare:
#     def creste(self):
#         print("Floarea creste")
#     def infloreste(self):
#         print("Floarea infloreste")
#     def miroase(self):
#         print("FLoarea miroase")
# class Floricica:
#     def creste(self):
#         print("Floricica creste")
#     def infloreste(self):
#         print("Floricica infloreste")
#     def miroase(self):
#         print("Floricica miroase")

# x = Floare
# y = Floricica

# for created_instance in [x, y]:
#     created_instance.creste(self)
#     created_instance.miroase(self)
#     created_instance.infloreste(self)

# from abc import ABC, abstractmethod
#
# class Floare(ABC):
#     @abstractmethod
#     def infloreste(self):
#         pass
# class Floricica(Floare):
#         pass
# class Flori(Floare):
#     pass
#
# created_instance = Floricica()
# created_instance.infloreste()
#
# from oop.inheritance import Main
# from oop.aggregation import Employee
# from abc import ABC, abstractmethod


class Car:
    def __init__(self, color, brand, utility):
        self.color = color
        self.brand = brand
        self.utility = utility

class Ford (Car):
    def caracteristici_F(self,color = "red",brand = "Ford",utility = "xyz" ):
        print("red","Ford", "xyz")
class Toyota(Car):
    def caracteristici_T(self, color="blue", brand="Toyota", utility="Privat"):
        print("")
class Volswagen(Car):
    def caracteristici_V(self, color="green", brand="Volswagen", utility="All utilities"):
        print("")

created_instance =Toyota("blue", "Toyota", "Privat")
print(created_instance.color)
print(created_instance.brand)
print(created_instance.utility)

x = Ford("red","Ford","xyz")
print(x.color)
print(x.brand)
print(x.utility)
y = Ford()






# print(created_instance)
# print(Car)
# print(created_instance.color)


















