#  Python Dictionaries 101: A Detailed Visual Introduction

ages = {"Xy": 15, "Io": 60}
print(ages["Io"])
print(ages["Xy"])

ages = {"SD": 56, "Uy": 78}
print(ages["SD"])
print(ages["Uy"])
# print(ages["GH"]) Error
ages["HY"] = 56
print(ages)
ages["Sy"] = 8
print(ages)

ages = {"Sf": 89, "IJI": 1}
ages["Sf"] = 52
print(ages)

ages = {"DF": 50, "TY": 10}
del ages["DF"]
print(ages)

ages = {"GY": 5, "IO": 51, "Mt": 4, "Ed": 12}
print("GY" in ages)  # True
print("KO" in ages)  # False
print(5 in ages)  # False. You can verify only if the key exist, not the value.
print(51 in ages.values())  # True. For values : key.values()
print(4 in ages.values())
print(len(ages))


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

ages = {"Ds": 45, "Jk": 15, "Ji": 2}
for key,value in ages.items():
    print("key:", key, ";value:",value)



ages = {"Af":50, "Ds":2, "Fg":8}
for key,     print("Key:"











