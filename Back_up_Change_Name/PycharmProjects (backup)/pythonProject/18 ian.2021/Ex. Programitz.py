saptamana = "astazi este marti."
x = saptamana.capitalize()
print(x)

string = "is an operator."
new_string = string.capitalize()
print("Abc:", new_string)

abc = "Python is awesome"
defg = abc.center(25)
print("Sir centrat:", defg)

jojo = "Python is awesome"
jojojo = jojo.center(20, "*")
print(jojojo)

koko = "PYTHON IS AWESOME"
print("Sir de caractere cu litere mici:", koko.casefold())

mesaj = "Python este un limbaj de prigramare foarte bun"
print("Numarul de aparitii a u", mesaj.count('u'))

Factura = "Electricitatea este de baza. Electricitatea..."
substracting = "Electricitatea"

count = Factura.count(substracting)
print("Cuvantul cheie este reptat de", count)

a = " competente digitale"
substracting = "digitale"

count = a.count(substracting)
print("Key word", count)

a = "Luna in cascade"
print(a.endswith("de"))
print(a.endswith("adidas"))
print(a.endswith("in cascade"))

a = " Python este un program IT"
resultat = a.endswith("IT", 10)
print(resultat)

result = a.endswith("este", 5, 26)
print(result)

resultatele = a.endswith("program", 2,30)
print(resultatele)


z = "In\tvederea\tinformarii\tcu\tprivire\tla\tmasurile\t"
print(z)

f = "In\nvederea\ninformarii\ncu\nprivire\nla\nmasurile\n"
print(f)

str = "abc\n12345\ntabc\n"
print("Original String : ", str)

print("Tabsize 2:", str.expandtabs(2))
print("Tabsize 3:", str.expandtabs(3))
print("Tabsize 4:", str.expandtabs(4))
print("Tabsize 5:", str.expandtabs(5))
print("Tabsize 6:", str.expandtabs(6))
print("Tabsize 6:", str.expandtabs(7))
print("Total", str.expandtabs(8))

abc = "Acesta este un cantec"
#change enconding to utf-8
print(abc.encode)

z = "Soarele cantand"
print(z.encode)

a = "În acest tutorial, vom afla despre metoda Python String encode() cu ajutorul exemplelor. "
print(a.encode)

string = "python!"
print("This string is:", string)
string_utf = string.encode()

print("The encoded version is:", string_utf)
print("The encoded version (with ignore) is:",string.encode("ascii","ignore"))
print("The encoded version (with replace) is:",string.encode("ascii","replace"))

b = "codarea informatiilor"
print("Acum von incerca :", b)
string_utf = string.encode()
print("Acum vom incerca:", string_utf)

b = " Acum vom incerca codarea informatiilor"
print(b.encode)

abc = "Buna varianta rea"
print(abc.find("rea"))

a = "Nebunul de alb"
y = 256415.2894584


print("Buna {n}, your balance is {y}. " .format(n="Nebunul de alb", y = 256415.2894584))

print("Buna {n}, your balance is {y:12f}." .format(n="Nebunul de alb", y= 256415.289458))
print("Buna {n}, your balance is {y:1.2f}." .format(n="Nebunul de alb", y= 256415.28945))












