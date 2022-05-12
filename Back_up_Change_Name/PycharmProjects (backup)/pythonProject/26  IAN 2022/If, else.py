
x: str = "Expected result"
y: str = "Actual result"
if x == y:
    print("Test passed")
else:
    print("Test Failed")
print(type(x))
print(type(y))

x: str = "Expected result"
y: str = "Actual result"
if x != y and type(x) == type(y):
    print("Test passed")
else:
    print("Test Failed")
print(type(x))
print(type(y))

x: str = "Expected result"
y: str = "Actual result"
if x != y and type(x) == type(y):
    if type(x) is str:
        print("Test passed")  # nested if
else:
    print("Test Failed")
print(type(x))
print(type(y))

x: str = "Expected result"
y: str = "Actual result"
if x != y and type(x) == type(y):
    if type(x) is int:
        print("Test Failed")  # nested if
    elif type(x) is str:
        print("Succes")
    else :
        print("Test passed")
else:
    print("Test Failed")
print(type(x))
print(type(y))

# elif - e o alta ramura in care rezultatul e fals.
# else - daca nu e stanga e dreapta. (Ne ajuta sa punem mai multe conditii inlantuite.)
# in Nested if se mai pot adauga la infinit if.


x: str = "Expected result"
y: str = "Actual result"
if x != y and type(x) == type(y):
    if type(x) is int:
        print("Test 2 Failed")  # nested if
    elif type(y) is str:
        print("Test 2. Succes!")
        if type(y) is int:
            print("Test 2 Failed")
        elif type(y) is str:
            print("Test 2. Succes!")
    else :
        print("Test 2 passed")
else:
    print("Test Failed")
print(type(x))
print(type(y))

