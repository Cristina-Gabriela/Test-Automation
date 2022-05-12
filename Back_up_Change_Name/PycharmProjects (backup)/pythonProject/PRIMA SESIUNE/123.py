

expected_pwd: str = "123abc"

pwd = input("Please enter a valid password: ")
assert pwd == expected_pwd
print(expected_pwd)

pwd = input("Please enter a valid password cu *: ")
assert pwd == expected_pwd
z = expected_pwd.replace("123abc","******")
print(z)
