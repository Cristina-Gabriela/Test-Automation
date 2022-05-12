def jessie():
    # code here gets executed when you call the function
    print("Arf arf")


jessie()


def jessie(mood, name):
    print(mood)
    print(name)
    if mood == "happy":
        print("Arf arf")
    else:
        print("whimper*")


jessie("happy", "Jessie")
jessie("sad", "Jessie")
jessie("angry", "Jessie")


def jessie(mood="happy"):
    print(mood)
    if mood == "happy":
        print("Arf, Arf")
    else:
        print("*whimper*")


print("first time")
jessie("happy")
print("\nsecond time")
jessie("sad")


def people(mood, name, options="subjective"):
    print(mood)
    print(name)
    print(options)

    if mood == "great":
        print("The mood of people are great.")
    else:
        print("The mood of people are not great.")


print("\nFirst of all:")
people("great", "People X", options="subjective")

print("\nSecond of all:")
people("bad", "People Y", options="subjective")


def add_one(x):
    return x + 1


y = add_one(5)
print(y)


def multiply_number(x):
    return x ** x


a = multiply_number(10)
print(a)


def add_number(d):
    return d + 25


print(add_number(50))


def multiply(b):
    return b ** 25


print(multiply(56))


def add_number(a, b):
    return (a + b) * (a + b) + 5 + 15 + 2 ** 3 / 2


print(add_number(10, 10))
