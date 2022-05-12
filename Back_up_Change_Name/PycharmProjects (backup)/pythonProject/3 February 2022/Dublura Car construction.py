class cartier_rezidential:
    def __init__(self, utilitati, case, blocuri, locuri_de_munca, locuri_de_loisir):
        self._utilitati = utilitati  # proprietati pe care le poate avea un cartier rezidential.
        self._case = case
        self._blocuri = blocuri
        self._locuri_de_munca = locuri_de_munca
        self._locuri_de_loisir = locuri_de_loisir

    def cheltuieli(self, buget):
        if buget > 1000:
            print(f"In parametri normali {self._utilitati}")
        elif 56000000000000000000000000 > buget > 80000000000000000000000000:
            print(f"Putin deasupra parametrilor normali {self._utilitati}")
        else:
            print("Printam mai multi bani")












class rezidential:
    def __init__(self, aditionle):
        self._aditionale = aditionale

    def masini_case(self, masini=3):
        if masini > 0:
            print(f"Un garaj dublu {self._aditionale}")
        elif 2 > masini > 4:
            print(f"Dispozitive de supraetajare sau parcare subterana : {self._aditionale}")
        else:
            print(f"Parcare tip chinezesc : {self._aditionale}")

mobilitate = rezidential (3)

# constructie = cartier_rezidential("complete", 200, 200, 800000000000, 1200)
# constructie.cheltuieli(200000000)
# constructie.cheltuieli(2)
#
# # mobilitate = rezidential(2, 3,5)
# mobilitate.masini_case(1)
# mobilitate.masini_case(3)
# mobilitate.masini_case(5)
