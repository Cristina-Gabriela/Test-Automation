# Dictionare:
# {key:data}
my_dictionary = {
    5: "int",
    True: "boolean",
    "txt": 5,
    5.6: "flt"
}
print(my_dictionary["txt"])
print(my_dictionary[5.6])
print(my_dictionary[5])
print(my_dictionary[True])

# print(my_dictionary.keys())
# my_dictionary.update({5: "hello"})
# print(my_dictionary.keys())

for k, v in my_dictionary.items():
    if k == 5:
        print(f"Keys: {k}")
        print(f"Values:{v}")

my_dict = {
    "Users": [
        {
            "Username": "JOJO",
            "Password": "asdf123!",
            "email": "jojo@mail.com"},
        {
            "Username": "JxJx",
            "Password": "agrh139!",
            "email": "jxjx@mail.com"},
        {
            "Username": "yoioi",
            "Password": "uyio23@",
            "email": "yoioi@mail.com"},
        {
            "Username": "JaOaJaO",
            "Password": "hgf183!",
            "email": "jaoajao@mail.com",
            "home": [1, "Calea Victoriei", "Medgidia"]},
    ]
        "Administrator": {
             "user": "Admin",
             "password": "123abc",
             "email": "admin@mail.com"
    }
}

print(my_dict["Users"][2]["Home"][2])

for k, v in my_dictionary.items():
    if k == "Users":
        for user in v:
            print(user)
            for k2,v2 in user.items():
                print(k2)
                print(v2)
        print(f"Keys: {k}")
        print(f"Values:{v}")


#TO DO: