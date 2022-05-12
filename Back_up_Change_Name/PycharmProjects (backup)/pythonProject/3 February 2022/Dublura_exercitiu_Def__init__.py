class magazin:
    def __init__(self, produse):
        self._produse = produse

    def Detergenti(self, buget):
        if buget < 200:
            print(f"Buget insuficient pentru detergent: {self._produse}")
        elif buget < 2000:
            print(f"Bugetul probabil pentru detergent: {self._produse}")
        else:
            print(f"Suma introdusa este probabil gresita.")

x = magazin('Ariel')
x.Detergenti(0)
x.Detergenti(1000)
x.Detergenti(3000)
