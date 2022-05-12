my_dictionary = {
    "Persoane": [
        {
            "username": "KIKI",
            "password": "252sg@!",
            "adress": "Str.Aleea xzxzxzxz, Cluj",
            "email": "kiki@gmail.com"},
        {
            "username": "Vivi",
            "password": "2564@!12!",
            "adress": "Str.Calea cvcvcvc, Cluj",
            "email": "vivi@gmail.com"},
        {
            "username": "Bibi",
            "password": "154dshj@!#",
            "adress": "Str.Aleea dhdydhyso,Cluj",
            "email": "bibi@gmail.com"},
        {
            "username": "Fifi",
            "password": "25454sbh@!@",
            "adress": "Aleea Khsdsct, Cluj",
            "email": "fifi@mail.com"},

    ]
}

print(my_dictionary)
print(my_dictionary["Persoane"][2])
print(my_dictionary["Persoane"][1]["username"])
print(my_dictionary["Persoane"][2]["password"])
print(my_dictionary["Persoane"][3]["adress"])
print(my_dictionary["Persoane"][0]["email"])

for a, z in my_dictionary.items():
    if a == "Persoane":
        for x in z:
            print(x)

for a, z in my_dictionary.items():
    if a == "Persoane":
        for persoane in z:
            print(persoane)
            for a2, z2 in persoane.items():
                print(a2)
                print(z2)












