# class Cariera():
#     tool = "Laptop"
#
#     def __init__(self, ore, munca="da"):
#         # ATTRIBUTES
#         # WE TAKE IN THE ARGUMENT
#         # ASSIGN IT USING SELF.ATTRIBUTE_NAME
#
#         self.timpul_petrecut = ore
#         self.munca_depusa = munca
#
#     # OPERATIONS/ACTIONS---> METHODS
#     def invata(self, persoana):
#         print("Invata!")
#         print("Continua aceasta actiune!")
#         print(f"Invata", self.timpul_petrecut, "ore. Aceasta", persoana)
#         print("Continua aceasta actiune!{},draga {}.".format(self.munca_depusa, persoana))
#
#
# variabila = Cariera("100000", "da")
# print(type(variabila))
# variabila2 = Cariera(ore="200000", munca="multa munca")
# print(variabila2)
#
# print(variabila.timpul_petrecut)
# print(variabila.munca_depusa)
# print(variabila2.timpul_petrecut)
# print(variabila2.munca_depusa)
# print(variabila.tool)
# print(variabila2.tool)
# # variabila = Cariera(self.munca)
# # variabila.ore
#
# # variabila.invata()
# # variabila2.invata()
# variabila.invata("persoana")
# variabila2.invata("persoana")


class Rectangle():
    diagonala = 11

    def __init__(self, latime = 2, lungime = 10):
        self.l = latime
        self.L = lungime

    def aria(self):
        return self.l * self.L

    def suma_diagonalelor(self):
        return self.diagonala + self.diagonala

    def aria_suma_diagonalelor(self):
        return self.l * self.L + self.diagonala + self.diagonala


variabila = Rectangle()
print(variabila.L)
print(variabila.l)
print(variabila.diagonala)
variabila.aria()
x = variabila.aria()
print(x)
variabila.suma_diagonalelor()
print(variabila.suma_diagonalelor())
y = variabila.aria()
print(y)

print(variabila.aria_suma_diagonalelor())
