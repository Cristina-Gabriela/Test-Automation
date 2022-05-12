# Listele in Python pot sa cuprinda elemente de tipuri diferite
# Au dimensiune dinamica
fructe = ["mar", "banana", "portocala", 3, True]

# afisam o lista
print(fructe)
# accesam un element in functie de index
print(fructe[0])
print(fructe[2])
# adaugam un nou element
fructe.append("mar")
# suprascriem un element
fructe[0] = 'para'
# afisam o lista
print(fructe)

# declaram si initializam un dictionar

pret = {"Paine": 5, "Unt": 6, "Ulei": 10}

#printam un nou produs cu un pret
pret["Peste"] = 20
print(pret)

#aflam pretul
print(pret["Paine"])
print(pret.get("Paine"))

#actualizam pretul;
pret["Unt"]=8
print(pret)

pret.pop("Paine")
print(pret.get("Paine","Nu mai exista paine"))
print(pret)

temperatura = {"ianuarie" : 0, "februarie" : 5, "martie" : 10 }
print(temperatura)
temperatura["aprilie"] = 15
print(temperatura)

temperatura["mai"] = 20
print(temperatura)

temperatura["iunie"] = 25
print(temperatura)

temperatura["iulie"] = 30
print(temperatura)

temperatura["august"] = 35
print(temperatura)

temperatura["septembie"] = 28
print(temperatura)

temperatura["octombrie"] = 20
print(temperatura)

temperatura["noiembrie"] = 10
print(temperatura)

temperatura["decembrie"] = 0
print(temperatura)

temperatura.pop("ianuarie")
print(temperatura)

temperatura.pop("august")
print(temperatura)

temperatura.pop("iulie")
print(temperatura)

# in februarie cate grade sunt?

print(temperatura["februarie"])
print(temperatura["martie"])
print(temperatura["aprilie"])
print(temperatura["mai"])
print(temperatura["iunie"])
print(temperatura["februarie"])
print(temperatura["decembrie"])
print(temperatura["noiembrie"])
print(temperatura["octombrie"])

temperatura["februarie"] = 10
print(temperatura)

temperatura["decembrie"] = -25
print(temperatura)
















