myset = set()
myset.add(1)
print(myset)
myset.add(2)
print(myset)
myset.add(3)
print(myset)
myset.add(4)
print(myset)
myset.add(5)
print(myset)

lista = [1,2,3,4,5,5,4,5,4,5,6,4,7,5,9,1,1,1,1,2,2]
print(set(lista))

print("As dori sa cumpar:{0},{1},{2},{3}".format("imbracaminte","mancare","apartament","masina"))
print("Frigiderul contine: {c},{l},{z},{b}".format(l="lapte", z="zarzavaturi", b="branza", c="cascaval"))
print("Cumparaturi:{0},{1},{2}".format("a","b","c"))

cumparaturi= set()
cumparaturi.add("laptop")
cumparaturi.add("incaltaminte")
cumparaturi.add("palton")
cumparaturi.add("pantaloni")
cumparaturi.add("bluza")

print(cumparaturi)
print(len(cumparaturi))
x= len(cumparaturi) * "*" +" "+ "produse"
print(x)

pret = 265548.2654844489
print(pret)
print("Acesta este un pret fictiv: {p:1.2f}".format(p=pret))

lista_de_cumparaturi= ["paine","legume", "carne","legume","legume","fructe","fructe","paine",]
print(lista_de_cumparaturi.count("legume"))
print(lista_de_cumparaturi.count("paine"))
print(lista_de_cumparaturi.count("fructe"))
print(lista_de_cumparaturi.index("fructe"))
print(lista_de_cumparaturi.index("legume"))
print(lista_de_cumparaturi.index("paine"))

















