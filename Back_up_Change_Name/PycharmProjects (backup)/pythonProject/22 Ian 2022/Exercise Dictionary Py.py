dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
dict['born'] = -428
print(dict["born"])

dict = {"name": "Plato", "country": "Ancient Greece", "born": -427, "teacher": "Socrates", "student": "Aristotle"}
dict["work"] = ["Apology", "Phaedo", "Republic", "Symposium"]
print(dict)

dict = {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
dict["son's height"] = dict["son's height"] + 2
dict["son's weight"] = dict["son's weight"] + 1.75
print(dict)

dict = {"son's name": "Lucas", "son's eyes": "green", "son's height": 32, "son's weight": 25}
ans_1 = dict.items()
print(ans_1)

dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
ans_1 = dict.get("son's height")
ans_2 = dict.get("son's name")
ans_3 = dict.get("son's eye color")
print(ans_1)
print(ans_2)
print(ans_3)

dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
ans_1 = dict.get("son's age", 5)
print(ans_1)

dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
dict.clear()
print(dict)

dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
x = len(dict)
print(x)

dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
x = max(dict)
print(x)

dict = {"son's name": "Lucas", "son's eye color": "green", "son's height": 32, "son's weight": 25}
ans_1 = min(dict)

print(ans_1)

x = len("son's name")
y = len("son's eye color")
z = len("son's height")
v = len("on's weight")

print(x)
print(y)
print(z)
print(v)

car = {
    "brand": "Ferari",
    "model": "last generation",
    "year": 2022
}

print(car)
print(car["brand"])
print(car["model"])
print(car["year"])

z = car["model"]
print(z)
v = car.get("brand")
print(v)
y = car.items()
print(y)

car = {
    "brand": "Ferari",
    "model": True,
    "year": 2022,
    "colors": ["grey", "green"]
}

print(car)
print(len(car))
print(type(car))
y = car["colors"]
print(y)

car = {
    "brand": "Ferari",
    "model": "last generation",
    "year": 2022
}
x = car.keys()
print(x)
y = car.values()
print(y)

car = {
    "brand": "Ferari",
    "model": "last generation",
    "year": 2022
}
car["new"] = "BMV"
print(car)
car["colors"] = "red"
print(car)
car["years"] = 2021
print(car)
car.update({"model": 2019})
print(car)

car = {
    "brand": "Ferari",
    "model": "last generation",
    "year": 2022
}
if "brand" in car:
    print("Brand ok")
if "model" in car:
    print("Model ok")
if "colors" in car:
    print("colors ok")
else:
    print("Colors, new key")

del car["brand"]
print(car)
car.pop("model")
print(car)
car.popitem()
print(car)
car.clear()
print(car)

for x in car:
    print(x)
for x in car:
    print(car[x])

car = {
    "brand": "Ferari",
    "model": "last generation",
    "year": 2022
}
for x in car.values():
    print(x)
for x in car.keys():
    print(x)
for x in car.items():
    print(x)

x = car.copy()
print(x)

cos = {
    "fructe": {
        "nume": "mar",
        "pret": 100
    },
    "legume": {
        "nume": "telina",
                "pret": 100
},
"racoritoare": {
    "nume": "limonada",
    "pret": 100
},
}

print(cos)


fructe= {
        "nume": "mar",
        "pret": 100
}
legume= {
        "nume": "telina",
        "pret": 100
}
racoritoare= {
   		"nume": "limonada",
    	"pret": 100
}
cos = {
	"fructe" :fructe,
    "legume": legume,
    "racoritoare":racoritoare
}
print(cos)


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print()
