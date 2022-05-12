def hello(test, x=1, y=2):
    print(test, x, y)

hello(4, y=6)


def another_hello(*users):
    print(f"Hello users{[0]}")
    print(f"Hello users{[1]}")
    print(f"Hello users{[2]}")


another_hello("Cristina", "Gabriela")

def last_hello(**members):
    print(f"Hello {members['name']}")
    print(f"Hello {members['surname']}")
    print(f"Hello {members['email']}")



last_hello(name="Cristina", surname="Gabriela", email="xyz@gmail.com")







