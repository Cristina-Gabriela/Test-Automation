class Creatura:
    def __init__(self,nume,varsta):
        self.nume = nume
        self.varsta = varsta
    def vorbeste(self):
    def mananca(self):

class Om(Creatura):
    def vorbeste(self):

    def mananca(self):

    def interactioneaza_cu(self, nume_cealalta_persoana):
        self.nume_cealalta_persoana = nume_cealalta_persoana
        print(Om,self.nume_cealalta_persoana)


class Animal(Creatura):
    def naste(self):


class caine(Animal):
    def vorbeste(self):
        print("Ham, ham")
    def mananca(self):
        print("Cainele mananca !")
class pisica(Animal):

x = Creatura('b', 50)
print(x)