dictionar_1 = {
    "produs": ["ciocolata", "fructe"],
    "nume": "Jojo",
    "cantitate": 1,
}
dictionar_2 = {
    "Salar": "excelent",
    "Vacanta": "formidabila",
    "Asigurare": "maxima",
}

dictionar_1.update(dictionar_2)
print(dictionar_1)

merged_dictionar = {**dictionar_1, **dictionar_2}
print(merged_dictionar)

all = {**dictionar_1, **dictionar_2}
print(all)

a = {
    "cioco": 1000,
    "de toate": 1,
}

b = {
    "salar": "Excelent",
    "imobil": "ok",
    "asigurare": "maxim",
}

a.update(b)
print(a)
x = {**a, **b}
print(x)

a = {}
b = {}
g = {}
i = {}

a["capsuni"] = 100
a["cirese"] = 1000
a["zmeura"] = 100

b["kiwi"] = 100
b["clementine"] = 123
b["rodie"] = 500

g["ananas"] = 150
g["prune"] = 75
g["mere"] = 1000

i["pere"] = 500
i["cocos"] = 425
i["struguri"] = 1425

cos = {**a, **b, **g, **i}
print(cos)
print(sorted(cos))
print(sorted(cos.items()))
print(len(cos.items()))
print(cos.keys())
print(cos.values())
print(sorted(cos.values()))
x = a["mure"] = 520
print(a)
cos2 = {**a, **b, **g, **i}
print(sorted(cos2))
cos_all = sorted(cos2)
print(cos_all)
cos_all_fruits = str(cos_all)
print(cos_all_fruits)
print(cos_all_fruits.swapcase())

v = sorted(cos.items())
f = str(v)
print(f)
print(f.swapcase())

print(str(sorted(cos.items())))
print(str(sorted(cos.items())).swapcase())
print(str(sorted(cos.items())).upper())
print(str(sorted(cos.items())).title())
print(str(sorted(cos.items())).capitalize())
print(str(sorted(cos.keys())).upper())
print(str(sorted(cos.keys())).lower())
print(str(sorted(cos.values())))
print(str(cos.values()))

for key, value in cos.items():
    print("Fructe:", key, "; Cantitate:", value)

s = {"abc  defg   hijk"}
r = str(s)
print(r.lower())
print(r.swapcase())
print(r.split())
print(r.splitlines())
print(r.title())

a = "SDFGH  cfdsf   fdfvd"
print(a.lower())
print(a.swapcase())
print(a.split())
print(a.splitlines())
print(a.title())

pret = {}.fromkeys(["capsuni","cirese","zmeura","kiwi","clementine"],20)
print(pret)
