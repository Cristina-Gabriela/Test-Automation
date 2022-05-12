# """
# Test bank account exercise :
# """
# expected_user: str = "Cristina"
# expected_pwd: str = "123abc"
# expected_sold: str = "100"
# # Implement the first test-case
# usr = input("Please enter a valid username: ")
# assert usr == expected_user
# print(type(expected_sold))
#
# pwd = input("Please enter a valid password: ")
# assert pwd == expected_pwd
# print(type(expected_pwd))
# print(expected_pwd)
#
# a = len(expected_pwd)
# print(len(expected_pwd))
# print(a)
#
# pwd = input(f"Your password has : {a} characters")
#
# pwd = input("Please enter a valid password cu *: ")
#
# assert pwd == expected_pwd
# z = expected_pwd.replace("123abc", "******")
# print(f"Your password is: {z}")
#
# pwd = input(f"Your password is : {z} and has {a} characters.")
#
# c = expected_pwd.replace("expected_pwd", "******")
# print(f"Your password is  : {c}")
#
# input("Please enter a login: ")
# print(f"Login successful! Your sold is : {expected_sold}")
# print("Login successful! Your sold is: " + str(expected_sold))
#
# cashback =str(input("Please enter the amount you want to retrieve:"))
# print(f"You have {float(expected_sold) - float(cashback)} euro left in your account")

'''
expected_user: str = "JOJO"
expected_password: str = "555aaa"
expected_sold: str = "200"

# Implement the first case-test:
user = input("Spune-ti numele:")
assert user == expected_user
print(type(expected_user))
print(expected_user)

password = input("Scrie parola:")
assert password == expected_password
print(type(password))
print(len(password))
print(expected_password)

sold = input("Scrie soldul fictiv")
assert sold == expected_sold
print(type(expected_sold))
print(len(expected_sold))

expected_password = len(expected_password) * "*"
print(expected_password)

expected_user = len(expected_user) * "*"
print(expected_user)

expected_sold = len(expected_sold) * "*"
print(expected_sold)

'''

a: str = "Evelina"
b: str = "500"
c: str = "5656aaa"

abc = input("Introdu numele: ")
bcd = input("Introdu suma: ")
cde = input("Introdu parola: ")

assert abc == a
assert bcd == b
assert cde == c

print(len(a))
print(len(b))
print(len(c))

print(len(a) * "#")
print(len(b) * "#")
print(len(c) * "#")
print(f"Numele dumneavostra este {a}, aveti in cont {b}, aveti parola {c}")

z = len(a) * "#"
s = len(b) * "#"
d = len(c) * "#"
print(f"Numele dumneavostra este {z}, aveti in cont {s}, aveti parola {d}")
print(f"Numele dumneavostra este {a}, aveti in cont {s}, aveti parola {d}")

cashback = str(input("Introdu suma pe care ai dori sa o retragi: "))
print(f'Mai ai in cont : {float(b)-float(cashback)} euro')
print(f"Vi s-au adaugat: {float(b) + float(10000)} euro la data de 15 ian 2022 ")


""" 
e-commerce ="Global Market"
login = ""
password = ""

"""


















