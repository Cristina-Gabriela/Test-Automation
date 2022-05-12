print("{:5d}".format(1212414542))
print("{:2.6f}".format(28))
print("{:20.3f}".format(12.5147))
print("{:08d}".format(25))
print("{:20.5f}".format(12.12))

print("{:+f} {:+f}".format(10.203, -14.23))
print("{:-f} {:-f}".format(12.25, 25.25))
print("{: f} {: f}".format(12.23, -56.56))
print("{: f} {: f} {: f}".format(-21.23, +56.23, 89.32))
print("{: f} {:-f} {:-f}".format(+21.23, -56.23, -89.32))

print("{:10d}".format(100))
print("{:6f}".format(200))
print("{:^25.2f}".format(51.2325625))
print("{:^20d}".format(253))
print("{:<100d}".format(2023))
print("{:=15.10f}".format(-56))

print("{:10}".format("dog"))
print("{:>10}".format("dog"))
print("{:^20}".format("dog"))
print("{:*^20}".format("dog"))

print("{:.6}".format("cantec"))
print("{:4.3}".format("cantec"))
print("{:^9.2}".format("cantec"))


class Cantec:
    a = 500
    b = "frumoase"


print("Cantecele sunt {b},au durat mai mult de {a} min.".format(b="frumoase", a="500"))

a = {"age":120, "name":"Jojo"}
print("{name} va avea {age} ani. ".format(**a))


























