expected_nume: str = "Cristina"
expected_password: str = "123"
expected_sold: int = "300"

nume = input("Afiseaza numele dorit:")
password = input("Afiseaza parola : ")
sold = input("Afiseaza soldul: ")

assert nume == expected_nume
assert password == expected_password
assert sold == expected_sold

input("Please enter a login : ")
print(f"Login successful ! Your sold is: {expected_sold}")

input("Please enter your password : ")
print(f"Login successful ! Your name is : {expected_nume}")


expected_product = "Imobiliare"
expected_country = "Elvetia"
expected_date = "01.02.2023"
product = input("Afiseaza sectorul cel mai profitabil")
country = input("Afiseaza tara cea mai buna din Europa")
date = input("Afiseaza data dorita")

assert product == expected_product
assert country == expected_country
assert date == expected_date

input("Afiseaza sectorul de activitate:")
print(f"Ai afisat cu succes ! Sectorul de activitate este : {expected_product}")

input("Afiseaza tara cu un nivel de trai foarte bun:")
print(f"Ai afisat cu succes! Tara cu cel mai mare nivel este : {expected_country}")

input("Afiseaza data dorita achizitionarii")
print(f"Ai afisat cu succes! Data achizitionarii este : {expected_date}")
