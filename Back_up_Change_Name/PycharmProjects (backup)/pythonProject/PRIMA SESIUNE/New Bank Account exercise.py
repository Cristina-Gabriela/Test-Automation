# Am declarat 3 variablile, am atribuit automat tipul de date pentru fiecare variabila, si i-am atribuit o valoare la fiecare variabila (intre ghilimele)
# Cu Alt Enter aflam tipul variabilei (integer, string, boolean, float).

expected_user: str = "Cristina"
expected_pwd: str = "123"
expected_sold: int = "100"
expected_cnp: int = "101213141516"

# user-ul , pwd, sold (variabila) primeste input de la tastatura, adica testerul sau/si dezvoltatorul introduce date in consola ca si cum ar fi intr-o interfata vizuala.

user = input("Afiseaza numele utilizatorului:")

# Pentru a valida variabila vom folosi o metoda in testare numita assert. Assert-ul compara automat ca un rezultat actual este egal cu unul sperat (expected_result).
assert user == expected_user

pwd = input("Afiseaza parola utilizatorului:")
assert pwd == expected_pwd

sold = input("Afiseaza soldul utilizatorului:")
assert sold == expected_sold

input("Please enter a login")
print(f"Login succesful! Your sold is: {expected_sold}")

input("Please enter your CNP")
print(f"Login successful! Your cont is activated : {expected_user}")
print("Login successful! Your cont is activated : " + str(expected_user))

# t(input("Please enter the amount you want to retrieve:"))
# rint(f"Login succesful! Your sold is: {expected_sold - cashback}")
# print(f"{expected_sold - a} euro left in your account")
cashback =str(input("Please enter the amount you want to retrieve:"))
print(f"You have {expected_sold - cashback} euro left in your account")

