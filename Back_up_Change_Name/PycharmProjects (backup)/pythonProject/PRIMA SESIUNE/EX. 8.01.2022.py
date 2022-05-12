expected_dezvoltare: str = "Tren TGV"
expected_regiune: str = "Dorohoi"
expected_data: str = "01.02.2023"

dezvoltare = input("Afiseaza proiectul de dezvoltare: ")
print(f"Ai afisat cu succes ! Proiectul de dezvoltare este: {expected_dezvoltare}")

regiune = input("Afiseaza regiunea de dezvoltare : ")
print(f"Ai afisat cu succes ! Regiune de dezvoltare este: {expected_regiune}")

data = input("Afiseaza data de incepere a lucrarilor: ")
print(f'Ai afisat cu succes ! Data de incepere a proiectului este: {expected_data}')

assert dezvoltare == expected_dezvoltare
assert regiune == expected_regiune
assert data == expected_data



