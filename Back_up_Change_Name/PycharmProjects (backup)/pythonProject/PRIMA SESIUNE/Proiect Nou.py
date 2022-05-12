""""
The bank account exercise
"""

expected_user: str = "nume"
expected_pwd: str = "123"
expected_sold: int = "100"

# implementing the first test case

user = input("Please enter a valid username:")
assert user == expected_user
print(type(expected_user)

pwd = input("PLease enter a valid password:")
assert pwd == expected_pwd
print(type(expected_pwd))

sold = input("Please enter a valid sold:")
assert sold == expected_sold
print(type(expected_sold))


