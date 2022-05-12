
x: str = "Expected result"
y: str = "Actual result"

if x == y and type(x) == type(y):
    print("True")
else:
    print("False")
    #print(type("False"))


x: str = "Expected result"
y: str = "Actual result"

if x != y and type(x) == type(y):
    print("True")
    if type(x) is str:
        print("str")
    elif type(x) is int:
        print("int")
else:
    print("False")


a: str = "Salariu bun"
b: str = "Motivatie crescuta"

if a != b and type(a) == type(b):
    print("Salariu bun este in corelatie cu motivatia crescuta")
    if type(a) is str:
        print("Se folosesc litere")
    elif type(a) is int:
        print("Se folosesc numere")
    elif type(a) is float:
        print("Nu se foloseste un numar intreg")

    if type(b) is str:
        print("Se folosesc litere si pentru b")
    elif type(b) is int:
        print("Se folosesc numere si pentru b")
    elif type(b) is float:
        print("Nu se foloseste un numar intreg si pentru b")
else:
    print("Cele doua nu sunt corelate")

