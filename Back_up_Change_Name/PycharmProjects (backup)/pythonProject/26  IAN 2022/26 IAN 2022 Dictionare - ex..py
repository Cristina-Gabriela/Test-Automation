#  Python Dictionaries 101: A Detailed Visual Introduction

# Access Values using Keys
ages = {"Xy": 15, "Io": 60}
print(ages["Io"])
print(ages["Xy"])

ages = {"SD": 56, "Uy": 78}
print(ages["SD"])
print(ages["Uy"])
# print(ages["GH"]) Error

# Add Key-Value Pairs
ages["HY"] = 56
print(ages)
ages["Sy"] = 8
print(ages)

# Modify a Key-Value Pair
ages = {"Sf": 89, "IJI": 1}
ages["Sf"] = 52
print(ages)

# Deleting a Key-Value Pair
ages = {"DF": 50, "TY": 10}
del ages["DF"]
print(ages)

# Check if a Key or Value is in a Dictionary
ages = {"GY": 5, "IO": 51, "Mt": 4, "Ed": 12}
print("GY" in ages)  # True
print("KO" in ages)  # False
print(5 in ages)  # False. You can verify only if the key exist, not the value.
print(51 in ages.values())  # True. For values : key.values()
print(4 in ages.values())

# Length of a Python Dictionary
print(len(ages))

# Iterating over Dictionaries (multiple options)
ages = {"Abc": 13, "Adsm": 44, "Sa": 5}
for student in ages:
    print(student)

ages = {"Ds": 45, "Jk": 15, "Ji": 2}
for student in ages.items():
    print(student)
for pair in ages.values():
    print(pair)
for pair in ages.keys():
    print(pair)

ages['Ds'] = 20
print(ages)

#  Assign Keys and Values to Individual Variables
ages = {"Ds": 45, "Jk": 15, "Ji": 2}
for key, value in ages.items():
    print("key:", key, ";value:", value)

ages = {"Ab": 20, "Cd": 60, "Fl": 50}
for name, age in ages.items():
    print("name:", name, "; age:", age)

curs_info = {"Ni": "dictionare", "Vi": "liste", "Bi": "pricipiile oop"}
for nume, curs in curs_info.items():
    print("nume:", nume, ";curs:", curs)

pret = {"legume": 5, "fructe": 6, "lactate": 10}
for produs, kg in pret.items():
    print("produs:", produs, ";kg:", kg)

cos = {"laptop": 1, "mouse": 1, "polar": 1}
for produs, cantitate in cos.items():
    print("produs:", produs, "; cantitate:", cantitate)

market = {"faina": 5, "mere": 10, "struguri": 2}
for cantitate in market.values():
    print("cantitate:", cantitate)
for produs in market.keys():
    print("Produsul:", produs)

# Dictionary Methods
print(market.get("mere"))
a = market.get("faina")
print(a)
v = market["faina"]
print(v)
print(market["faina"])
d = market.pop("struguri")
print(market)
h = market.popitem()
print(market)
market["ulei"] = 20
print(market)
produs_nou = {"ciocolata": 2}
market.update(produs_nou)
print(market)

raft_1 = {"ciocolata": 10, "cafea": 2, "detergent": 0}
produs_nou = {"napolitane": 2}
raft_1.update(produs_nou)
print(raft_1)
raft_1["ciocolata"] = 12
print(raft_1)
raft_1["capucino"] = 2
print(raft_1)
produs_1 = {"ulei_de_masline": 10}
raft_1.update(produs_1)
print(raft_1)




