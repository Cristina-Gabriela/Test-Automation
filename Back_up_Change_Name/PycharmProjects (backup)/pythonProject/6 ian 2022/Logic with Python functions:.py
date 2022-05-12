class Figure:
    figura = "Figure Class"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rectangle_area(self):
        pass

    @staticmethod
    def triangle_area():
        print("compute triangle area")

    def circule_are(self):
        return self.figura


Abc = Figure("a", "b")
print(Abc.figura)
Abc.triangle_area()
Abc.triangle_area()


def functia_clasa(mesaj):
    print(mesaj + " de la mine de acasa.")


functia_clasa("Buna")


def functia_clasa(mesaj_1, mesaj_2, mesaj_3):
    print("Buna, " + mesaj_2 + " " + mesaj_1 + " " + mesaj_3)


functia_clasa("Ce mai faci?", "O duci bine?", "Ce mai faci, inca o data?")


def functia_clasa(*mesaj):  # cand nu se stie cu exactitate numarul de argumente.
    print("Buna " + "" + mesaj[0])
    print("Buna " + "" + mesaj[4])
    print("Buna " + "" + mesaj[2])
    print("Buna " + "" + mesaj[1])
    print("Buna " + "" + mesaj[3])


functia_clasa("Ce mai faci ?", "O duci bine?", "Ce mai faci inca o data ?", "Esti bine?", "Cum iti este viata?")


def functia_clasa(mesaj_1, mesaj_2, mesaj_3, mesaj_4):
    print("Buna. " + mesaj_4)


functia_clasa(mesaj_1="Ce faci ?", mesaj_2="O duci bine?", mesaj_3="Cum mai este viata ta?",
              mesaj_4="Ce faci cu viata ta?")


def functia_clasa(**mesaj):
    print("Buna. " + mesaj["mesaj_in_interior"])


functia_clasa(mesaj_in_interior="Tu o duci bine, asa este ?")


def functia_clasa(mesaj="Ai o viata ok? "):
    print("Buna." + mesaj)


functia_clasa("Cine are o viata ok?")
functia_clasa("Ai o viata ok? ")
functia_clasa("Te prefaci ? ")
functia_clasa("Esti un actor ? ")


def functia_clasa(mesaj):
    for x in mesaj:
        print(x)


mai_multe_mesaje = ["Te prefaci", "Esti doar un actor", "Cum iti este viata?"]
functia_clasa(mai_multe_mesaje)


def functia_clasa(x):
    return 10 * x


print(functia_clasa(10))
print(functia_clasa(5))
print(functia_clasa(8))
print(functia_clasa(2))


def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def functia_clasa(mesaj):
    return 5 * mesaj


print(functia_clasa(21))
print(functia_clasa(123))
print(functia_clasa(7536741))
print(functia_clasa(7786))


def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n Acesta este un exemplu de recursivitate")
tri_recursion(10)


# Apelarea unei funcții

# Argumente  #  o funcție cu un singur argument

# Numărul de argumente

# Argumente arbitrare, *args

# Argumentele cuvintelor cheie

# Argumente de cuvinte cheie arbitrare, **kwargs  # Aici va primi un dictionar

# Valoarea implicită a parametrului

# Trecerea unei liste ca argument

# Valori returnate print

# Declarația de trecere











