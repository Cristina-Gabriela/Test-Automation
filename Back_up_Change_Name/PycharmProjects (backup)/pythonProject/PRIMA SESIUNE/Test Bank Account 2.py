"""
Test bank account exercise :
"""

expected_user: str = "Cristina"
expected_pwd: str = "123abc"
expected_sold: str = "100"
# Implement the first test-case
usr = input("Please enter a valid username: ")
assert usr == expected_user
print(type(expected_sold))

pwd = input("Please enter a valid password: ")
assert pwd == expected_pwd
print(type(expected_pwd))
print(expected_pwd)
print(len(expected_pwd))

print("*", end= " ")




input("Please enter a login: ")
print(f"Login successful! Your sold is : {expected_sold}")
print("Login successful! Your sold is:" + str(expected_sold))

cashback= int(input("Please enter the amount you want to retrieve: "))
print(f"You have {expected_sold - cashback} left in your account.")

