a = "Casa mea o e un cantec cu acorduri ample "
result = a.index("cantec")
print(result)

result = a.index("acorduri ample")
print("Substring 'acorduri ample':", result)
print(a.index("corduri", 10))

# islanum
a = "c,65454 nuuh kdoiosdi 2387"
print(a.isalnum())

b = "2133"
print(b.isalnum())

v = "bhdgy5645"
print(v.isalnum())

a = "4654518hdbf"
if a.isalnum() == True:
    print("Toate caracterele se incadreaza in isalnum")
else:
    print("Nu se incadreaza in aceasta functie")

a = "mciuhgubdciudbhb"
print(a.isalpha())

b = "furhguehf25438"
print(b.isalpha())

x = "2541cndhb"
if x.isalpha() == True:
    print("Toate caracterele sunt corecte")
else:
    print("Caracterele sunt si alfa si numerice")













