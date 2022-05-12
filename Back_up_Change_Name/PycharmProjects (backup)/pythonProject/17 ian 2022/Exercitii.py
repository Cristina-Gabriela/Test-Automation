
ghiozdan = ["caiete", "creion", "cheie"]
print(ghiozdan)

ghiozdan.append("mancare")
print(ghiozdan[2])
ghiozdan[2] = "mancare"
print(ghiozdan)
ghiozdan[3] = "fular_si_manusi"
print(ghiozdan)

corp = ["inima", "creier", "celula"]
print(corp)

corp.append("dinte")
print(corp)

corp[2] = "stomac"
print(corp)


lista = ["Ministerul Transporturilor și Infrastructurii", "Ministerul Finanțelor", "Ministerul Justiției"]
print(lista)

lista.append("Ministerul Apărării Naționale")
print(lista)

lista[1] = ("Ministerul Sănătății")
print(lista)

x = sorted(lista)
print(x)

print(len(lista))
print(lista.count("Ministerul Justiției"))

lista_noua = ["Ministerul Energiei", "Ministerul Agriculturii și Dezvoltării Rurale",
              "Ministerul Muncii Și Solidarității Sociale", "Ministerul Sportului",
              "Ministerul Mediului, Apelor și Pădurilor"]
lista.extend(lista_noua)
print(lista_noua)
print(lista)
d = sorted(lista)
print(d)

adaugat = ["Ministerul Cercetării, Inovării și Digitalizării"]
lista.extend(adaugat)
print(lista)
f = sorted(lista)
print(f)
print((len(f)))
v = len(f)
print(f"Numarul de ministere este: {v}" )

last = f.pop()
print("ultimul element:", last)

print(lista.count("Ministerul Transporturilor și Infrastructurii"))

























