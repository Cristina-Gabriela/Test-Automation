expected_vacanta: str = "Romania"
expected_personal: str = "toata familia"
expected_buget: str = "5000"

vacanta = input("Zona de calatorie: ")
personal = input("Numarul de persoane: ")
buget = input("Suma alocata:")

assert vacanta == expected_vacanta
assert personal == expected_personal
assert buget == expected_buget

print(f"Tara de vizitat : {expected_vacanta}")
print(f"Numar turisti: {expected_personal}")
print(f"Suma: {expected_buget}")
print(f"Taote informatiile: {expected_vacanta} {expected_personal} {expected_buget}")

if "a" == "a":
    print(True)
else:
    print(False)

num = 123
if num > 10:
    print("Numere intre 11 si 122")
    if num >1515:
        print("Numere intre 1516, plus infinit")