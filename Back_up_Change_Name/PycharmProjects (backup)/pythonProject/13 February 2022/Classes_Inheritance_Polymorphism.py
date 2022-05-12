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

class Vacanta:
    def __init__(self, title, passengers, budget):
        self.title = title
        self.passengers = passengers
        self.budget = budget

    # def __str__(self):
    #     print("Aceasta este vacanta cu titlul: " + self.title+ "Are  mai multe locuri" + self.passengers )

created_instance = Vacanta("La munte", "50","5000")
print(created_instance)   # what is string representation of created instance.
str(created_instance)











