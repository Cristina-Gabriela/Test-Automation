class Padure fermecata

zmei = nume
spiridusi = nume

zmei = superputeri(str)
spiridusi = inaltime, + un numar de urechi

# Padurea fermecata - numar limitat de locuri de vietuitori  - trebuie dat la constructori __init__

# o functie in Padurea Fermecata -- un zmeu si un spiridus
#
# cand loc limitat- print("Nu se poate adauga")
#
# Un zmeu poate sa atace un anumit spiridus
# un spiridus se poate apara la atacul unui zmeu -- o metoda de fiecare data cand zmeul ataca.
#
# De fiecare data cand exista un atac sa se afiseze ca atacul a avut loc
#
# Pt a determina cine a castigat, se va determina o variabila random intre 0 si unu
# Daca valoarea > 0.5, zmeul a castigat, ALtfel celalalt a castigat.
# SA se afiseze cine a castigat
#
# FIecare atac are un numar unuic, care tot creste.
# Daca zmeul are mai mult de 2 superputeri sa se foloseasca doar supersputerile cu indexul par.
#
# sa se afiseze ce superputeri s-au folosit.

import random

class Padure_fermecata:
    def __init__(self,max_locuri):
        self.max_locuri = max_locuri
        self.creaturi = []

    def adaugare_creatura(self,vietuitoare):

        if self.max_locuri <= max_locuri:
            print("Adauga vietuitoare")
        else:
            print('Nu se poate adauga')


class Zmeu:
    def __init__ (self,nume, superputeri):
        self.nume = nume
        self.superputeri = superputeri

    def atac (self,numar_z ):
        self.numar_z = numar_z

        if random():
            print("Atacul a avut loc")
        else:
            print("Atacul nu a avut loc")


class Spiridus:
    def __init__ (self, nume,inaltime, numar_de_urechi):
        self.nume = nume
        self.inaltime = inaltime
        self.numar_de_urechi = numar_de_urechi

    def atac (self, numar_s):
        self.numar_s = numar_s

        if :
            print("Atacul a avut loc")
        else:
            print("Atacul nu a avut loc")

a = random.random()
for i in range(2):
    print(random.random())
    if a > 0.5:
        print("Zmeul a castigat !")
    else:
        print("Spiridusul a castigat !")


max_locuri = int(input("Introdu numarul maxim de locuri"))
x = Zmeu("Z", 10)
y = Spiridusi("S",2.5, 2)

x2 = Zmeu()
y2 = Spiridus()

y3 = Spiridus()

self.max_locuri = 3


x.Padure_fermecata
y.Padure_fermecata




def Functie(a, b, c):
    if len(a) < b:
        a.append(c)
        print(a)
        return a
    else:
        print("Mesaj de eroare")
        return a


x= Functie([7, 8, 9], 100, 1)
print(x)

x= Functie([7, 8, 9], 2, 1)
print(x)



Functie([], 1, 2)
Functie([2, 3, 5, 6, 8, 9, 4, 5, 4], 4, 14)

functie care primeste o lista de numere si 2 parametri
numar max  de elemente pe care il poate avea lista
al treilea parametru = element de adaugare
returnezi
