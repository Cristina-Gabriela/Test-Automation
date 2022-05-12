# Clase - sunt "tipare".
# metode - apartenenta la o clasa.  # are acces la orice element din interiorul clasei.
# Pentru a crea o metoda trebuie sa apelam un obiect.

def sum(a, b):
    return a + b


def dif(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum(self):
        return self._a + self._b

    #    def sum(self, a, b):
    #        return a + b

    def dif(self):
        return self._a - self._b

    #   def dif(self, a, b):
    #       return a - b

    #   def inmultire(self, a, b):
    #       return a * b
    def inmultire(self, c):
        return self._a * self._b * c

    @staticmethod  # orice metoda este o functie. Metodele de instanta au nevoie de un obiect pentru a fi apelate.Nu depind de clasa respectiva. Nu sunt sub aceeasi umbrela.
    def impartire(a, b):
        return a / b


my_calculator = Calculator(3,2)  # clasa nu are valoare daca nu capata viata. Obiectul este masina, un mic calculator de buzunar, etc. Prin acel obiect putem sa facem cateva functionalitati.

print(my_calculator.sum())
print(my_calculator.dif())
print(my_calculator.impartire(10, 5))
print(my_calculator.inmultire(5))




