pret = {"creion": 2, "carioca": 5}
print(pret)

print(pret["creion"])
pret["rigla"] = 10
print(pret)

pret["creion"] = 3
pret["carioca"] = 5.1
pret["rigla"] = 10.2
print(pret)

pret.pop("carioca")
print(pret)

x = sorted(pret)
print(pret)

#from typing import Tuple
a = 5
print(a ** a * a ** a)

a = ("Ana\nare\nmere")
print(a)

print(len("hello"))
print(len("hello the"))

name = "Sam are multe mere"
last_letters = name[1:]
print(last_letters)
last_letters = name[4:]
print(last_letters)
last_letters = name[8:]
print(last_letters)
last_letters = name[0:3]
print(last_letters)
last_letters = name[4:50:2]
print(last_letters)
a = "D" + "u" + last_letters + "ie"
print(a)

f = "Parola\n"
print(f * 200)

f = "Parola\t"
print(f * 200)

x = "luni este prima zi a saptamanii"
print(x.upper())
print(x.casefold())
print(x.capitalize())
print(x.isalnum())
print(x.isascii())
print(x.isdigit())
print(x.isidentifier())
print(x.title())
print(x.__sizeof__())
print(x.__repr__())
print(x.__getnewargs__())
print(x.lower())
print(x.swapcase())
print(x.__dir__())
print(x.__eq__(x))

abcd = "Cipru\n55.7\nIrlanda\n49.1\nAruba\n48.4\nAndorra\n45.2\nIslanda\n43.3\nFranța\n42.2\n"
print(abcd.split())

abc = "Hello world ! Buna lume!"
print(abc.split())

numar = "25242829262724212121232526"
print(numar.split("2"))

print("Cosul de cumaparaturi contine: {0} {2} {0} {2} {0}".format("paine", "esenta de vanilie si rom", "faina", "cacao",
                                                                  "praf de copt"))

print("Frigiderul contine: {},{},{},{}".format("lapte", "zarzavaturi", "branza", "cascaval"))
print("Frigiderul contine: {2},{3},{0},{1}".format("lapte", "zarzavaturi", "branza", "cascaval"))

print("Frigiderul contine: {b},{c},{l},{z}".format(l="lapte", z="zarzavaturi", b="branza", c="cascaval"))
print("Frigiderul contine: {c},{l},{z},{b}".format(l="lapte", z="zarzavaturi", b="branza", c="cascaval"))

rezultat = 23.25484864354561852
print("Acesta este: {r:1.3f}".format(r=rezultat))

suma: float = 555.2323548974865845666664
print("Suma pe care am calculat-o este de :{s:1.1f}".format(s=suma))

nume = "Ana", "Angela", "Aghel", "Didi"
print("Numele celor de pe lista sunt:{n},{n},{l},{d}".format(a="Ana", n="Angela", l="Anghel", d="Didi"))



dictionar = {"A1":100, "B1":200, "C1":300}
print(dictionar.keys())
print(dictionar.values())








