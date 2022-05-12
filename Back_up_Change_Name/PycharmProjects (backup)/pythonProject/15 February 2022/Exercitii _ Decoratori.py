# return a function with another function
#
# def func():
#     return 1
#
#
# print(func())
# print(func)
#
# def hello():
#     return "Hello!"
# print(hello())
# print(hello)
#
# created_instance = hello
# print(created_instance())
# print(hello())
# del hello
#
# def hello(name="Jose"):
#     print("First: The hello() function has been executed !")
#
#     def greet():
#         return "\t Second : This is the greet() func inside hello !"
#
#     def welcome():
#         return "\t Third : This is welcome() inside hello"
#
#     print('Final: I am going to return a function ! ')
#     # print(greet())
#     # print(welcome())
#     # print("This is the end of the hello function !")
#
#     if name == "Jose":
#         return greet
#     else:
#         return welcome
#
# created_instance = hello("Jose")
# print(created_instance())
#


# print(hello())
# print(hello)
# hello()
# print("")
# created_instance = hello()
#
# def bunastare(name = "pentru Cristina"):
#     print("Prima propozitie. Cristina vrea bunastare.")
#
#     def lucru():
#         return "Cristina inca nu are bunastare."
#
#     def salariu():
#         return "Cristina nu are salariu momentan."
#
#     if name == "Cristina":
#         return lucru
#     else:
#         return salariu
#
# created_instance  = bunastare("pentru Cristina")
# print(created_instance())


#
# def Bank_Account(valuta = 10):
#     print("This is your sold")
#
#     def venituri():
#         print("Contul inregistreaza venituri")
#     def cheltuieli():
#         print("Contul inregistreaza cheltuieli")
#
#     if valuta == 100:
#         return venituri
#     else:
#         return cheltuieli
#
# created_instance = Bank_Account(10)
# created_instance()

# def Account():
#
#     def venituri():
#         return "Ar fi foarte bine !"
#
#     return venituri
#
# instance = Account()
# print(instance())
#

def new_decorator(original_func):
    def wrap_func():
        print("SIA, Courage to change")
        original_func()
        print("Never be enough")

    return wrap_func()


def func_needs_decorator():
    print("I want to listen the music")


func_needs_decorator()
print("")

my_instance = new_decorator(func_needs_decorator())

sa
se
creeze
o
clasa
abstracta
numita
creatura
care
are
2
filecmp, varsta
si
nume
si
care
are
2
metode
abstracte
vorbeste
si
mananca,
sa
se
creeze
2
copii
ale
acestei
creaturi(ale
clasei
creatura): om
si
animal, clasa
animal
este
si
ea
la
randul
ei
abstracta, si
mai
are
un
parametru, metoda
nasterii - poate
fi
din
animal - - din
clasa
abstracta, vor
deriva
inca
2
clase - caine
si
pisica.Sa
se
suprascrie
comportamentul
functiilor
din
clasele
abstracte, in clasele
copii.De
ex.cand
se
apeleaza
metoda
caine, sa
se
afiseze
ham - ham, cand
se
apeleaza
metoda
mananca, sa
se
afiseze
cainele
mananca, iar
pentru
clasa
persoana
sa
se
suprascrie
metodele
necesare
ca
clasa
sa
poata
fi
implementata, deci
trebuie
sa
implementeze
metodele
abstracte, pe
care
le
ia
din
clasa
creatura, si
apoi
sa
se
defineasca
o
noua
functie
care
sa
se
numeasca
interactioneaza
cu
si
care
sa
primeasca
parametru
o
alta
persoana
si
sa
se
afiseze
persoana
curenta - vorbeste
cu
persoana
cealalta
care
o
primeste
ca
parametru.Se
foloseste
persoana.nume(numele
persoanei in afisare.) Trebuie
sa - instantiezi - persoane
de
tipul
claselor
concrete - adica
persoana
caine
si
pisica
si
sa
apelezi
toate
metodele
pe
care
le
au
la
dispozitie.


class Salariu:
    def __init__(self, persoana):
        self.persoana = persoana

        self.timp = []
        self.concediu = []
        self.asigurare = []

    def add_salariu(self, prime):
        self.timp.append(prime)
        self.concediu.append(prime)
        self.asigurare.append(prime)

    def add_vacanta(self, bonuri):
        self.concediu.append(bonuri)

class 2