# Dictionary:
# {key:data}

my_dictionary = {
    5: int,
    5.2: "flt",
    True: "boolean",
    "txt": 255
}

print(my_dictionary[5])
print(my_dictionary[5.2])
print(my_dictionary[True])
print(my_dictionary["txt"])
print(my_dictionary.get(True))
print(my_dictionary.update({"true": "hello"}))
print(my_dictionary)
print(my_dictionary.update({"txt": 500}))
print(my_dictionary)
print(my_dictionary.update({"5.6": "float"}))
print(my_dictionary)

for k, v in my_dictionary.items():
    if k == 5:
        print(f"keys:{k}")
        print(f"values:{v}")
for a, b in my_dictionary.items():
    if a == 5.2:
        print(f"keys:{a}")
        print(f"values:{b}")
for c, d in my_dictionary.items():
    if c == True:
        print(f"keys:{c}")
        print(f"values:{d}")
for o, y in my_dictionary.items():
    if o == "txt":
        print(f"keys:{o}")
        print(f"values:{y}")

my_dictionary = {
    "Users": [
        {
            "username": "JOJO",
            "Password": "dnndcA626@@!$#j",
            "email":"jojp@mail.com"},
        {
            "username": "XYZZ",
            "Password": "1c#fiAeh$#f532",
            "email":"xyzzp@mail.com"},
        {
            "username": "YOIYOI",
            "Password": "281jdcA2@&(*&0",
            "email":"yoiyoi@mail.com"},
        {
            "username": "DAZFUOL",
            "Password": "846jAdc2@&(*&0",
            "email":"dazfuol@mail.com",
            "home": [123, "Calea Victoriei", "Medgidia"]},
    ],
    "Admin": {
        "user": "Admin",
        "password": "652fjAdh@!$*5",
        "email":"admin@mail.com",
    }
}

print(my_dictionary)
print(my_dictionary["Users"][3]["home"][1])
print(my_dictionary["Users"][3]["username"])
print(my_dictionary["Users"][1]["Password"])
print(my_dictionary["Users"][0]["email"])
print(my_dictionary["Users"][1]["email"])
print(my_dictionary["Users"][2]["email"])
print(my_dictionary["Users"][3]["email"])
print(my_dictionary["Users"][0]["username"])
print(my_dictionary["Users"][1]["username"])
print(my_dictionary["Users"][2]["username"])
print(my_dictionary["Users"][3]["username"])
print(my_dictionary["Users"][0]["Password"])
print(my_dictionary["Users"][1]["Password"])
print(my_dictionary["Users"][2]["Password"])
print(my_dictionary["Users"][3]["Password"])
print(my_dictionary["Admin"])
print(my_dictionary["Admin"]["email"])
print(my_dictionary["Admin"]["password"])
print(my_dictionary["Admin"]["user"])

for a, z in my_dictionary.items():
    if a == "Users":
        for x in z:
            print(x)

for a, z in my_dictionary.items():
    if a == "Users":
        for user in z:
            print(user)
            for a2, z2 in user.items():
                print(a2)
                print(z2)
