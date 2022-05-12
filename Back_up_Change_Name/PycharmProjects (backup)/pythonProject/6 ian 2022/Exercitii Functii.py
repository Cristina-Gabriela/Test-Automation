# Apelarea unei funcții
def functie():
    print("Te simti bine?")


functie()


# Argumente  #  o funcție cu un singur argument
def functie(mesaj):
    print("Intrebare:" + mesaj)


functie("Te simti bine?")


# Numărul de argumente
def functie(mesaj):
    print("Intrebare: " + mesaj)


functie("Te simti bine?")


# Argumente arbitrare, *args
def functie(*mesaj):
    print("Intrebare:" + mesaj[0])
    print("Intrebare:" + mesaj[1])
    print("Intrebare:" + mesaj[2])
    print("Intrebare:" + mesaj[3])
    print("Intrebare:" + mesaj[1])
    print("Intrebare:" + mesaj[2])


functie("Te simti bine?", "Ce venituri ai?", "Traiesti bine?", "Cata scoala sa mai fac pentru o bucata de paine? ")


# Argumentele cuvintelor cheie
# def function(a, b, c, d):
#
#
# print("Intrebare:" + a)
# print("Intrebare:" + b)
# print("Intrebare:" + c)
# print("Intrebare:" + d)
#
# functie(a = "Te simti bine?", b = "Ce venituri ai?", c = "Traiesti bine?", d = "Cata scoala sa mai fac pentru o bucata de paine? "  )
#
#


# Argumente de cuvinte cheie arbitrare, **kwargs  # Aici va primi un dictionar
def functie(**mesaj):
    print("Intrebare:" + mesaj["mesaj_1"])
    print("Intrebare:" + mesaj["mesaj_2"])
    print("Intrebare:" + mesaj["mesaj_3"])
    print("Intrebare:" + mesaj["mesaj_4"])


functie(mesaj_1="Te simti bine ?", mesaj_2="Ce venituri ai ?", mesaj_3="Traiesti bine ?",
        mesaj_4="Cata scoala sa mai fac pentru o bucata de paine ?")


# Valoarea implicită a parametrului
def function(mesaj_1="Te simti bine?"):
    print("Intrebare:" + mesaj_1)


function()


# Trecerea unei liste ca argument
def function(mesaj):
    for x in mesaj:
        print(x)


intrebare = ["Te simti bine?", "Ce venituri ai ?", "Traiesti bine ?",
             "Cata scoala sa mai fac pentru o bucata de paine ?"]
function(intrebare)


# Valori returnate print
def function(msg):
    return (5 * msg)

print(function("Te simti bine?\n"))

# Declarația de trecere
def function():
    pass