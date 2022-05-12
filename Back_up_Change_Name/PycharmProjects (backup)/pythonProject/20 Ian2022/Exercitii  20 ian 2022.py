a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.zfill(10))
print(a.zfill(100))

s = "-23.56"
print(s.zfill(50))
print(s.startswith("-2"))

d = "--random+text"
print(d.zfill(100))
print(d.startswith("--"))

a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.title())

x = "t g v romania 20 01 2022"
print(x.title())
print(x.startswith("t g v"))

import re


def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z)]+)?",
                  lambda mo: mo.group(0)[0].upper() +
                             mo.group(0)[1:].lower(),
                  s)


text = "He's an engineer, isn't he?"
print(titlecase(text))
print(text.startswith("He's an"))
print(text.startswith("engineer"))

a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.startswith("TGV"))
print(a.startswith("cel mai amplu"))
print(a.startswith("TGV-ul cel mai amplu proiect"))
result = a.startswith("TGV-ul cel mai amplu proiect")
print(result)
result = a.startswith("proiect de dezvoltare", 21)
print(result)
result = s.startswith("a automatizarii", 50)
print(result)
result = a.startswith("de dezvoltare a automatizarii", 29, 58)
print(result)
s = "de dezvoltare a automatizarii"
print(len(s))

z = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(len(z))
result = z.startswith("TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania.", 0, 70)
print(result)

z = "TGV-ul\ncel mai amplu proiect de dezvoltare\n a automatizarii\n in Romania."
print(z)

v = "TGV-ul\rcel mai amplu proiect de dezvoltare\r a automatizarii\r in Romania."
print(v)

k = "TGV-ul cel mai amplu proiect de\r dezvoltare a automatizarii in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\r\n dezvoltare a\r\nautomatizarii in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\x0b dezvoltare a automatizarii in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\v dezvoltare a automatizarii\v in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\f dezvoltare a automatizarii\f in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\x1c dezvoltare a automatizarii\x1c in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\x1d dezvoltare a automatizarii\x1d in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\x1e dezvoltare a automatizarii\x1e in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\x85 dezvoltare a automatizarii\x85 in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\u2028 dezvoltare a automatizarii\u2028 in Romania."
print(k)
k = "TGV-ul cel mai amplu proiect de\u2029 dezvoltare a automatizarii\u2029 in Romania."
print(k)

a = "TGV-ul\n cel mai\r\n amplu proiect de dezvoltare\r a automatizarii\rin\n Romania."
print(a.splitlines())
print(a.splitlines(True))
print(a.splitlines())
print(a[2])
print(a[0:4])
print(a[14:31])
print(len("amplu proiect de dezvoltare"))
print(len("TGV-ul cel mai"))
print(27 - 14)

a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a[:-50])
print(a[:50])
s = len("Romania")
print(s)
print(a[-8:])

a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.rsplit())
print(a[-8:])
print(a[:3])
a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.rsplit(',', 10))
a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.split())
print(a.split(',', 5))

a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.rindex("amplu"))
print(a.rindex("dezvoltare"))
print(a.rindex("Romania"))
print("Substring'TGV':", a)
print(a.rindex("V"))
v = a.rfind("amplu")
print("Substring 'amplu': ", v)
h = a.rfind("dezvoltare")
print("Pozitia la care se afla cuvantul dezvoltare este:", h)
d = a.rfind("automatizarii")
print("Automatizarea incepe de la pozitia:", d)

result = a.rfind('automatizarii')
if (result == 45):
    print("True")
else:
    print("False")

result = a.rfind("dezvoltare")
if (result == 32):
    print("True")
else:
    print("False")

result = a.rfind("TGV")
if (result != 20):
    print("!=20")
else:
    print("==20")

a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
print(a.rfind("proiect", 5))
v = a.rfind("Romania")
print(v)

a = "TGV-ul cel mai amplu proiect de dezvoltare a automatizarii in Romania."
replaced_text = a.replace("Romania", "toata lumea")
print(replaced_text)

a = "ceas, ora, 10"

replaced_text = a.replace("ceas", "orologiu")
print(replaced_text)
print(a.split())
print(a.zfill(50))
print(a.upper())
print(a.lower())
print(a.swapcase())
print(a.title())
print(a.strip())
print(a.startswith("or"))
print(a.startswith("ce"))
print(a.splitlines())
print(a.split())
print(a.rstrip())
print(a.rpartition("ora"))
print(a.capitalize())
print(a.casefold())
print(a.center(20))
print(a.encode())
print(a.endswith("ra"))
print(a.expandtabs())
print(a.find("ora"))
print("Am cumparat un {0} la {1} 14.".format("ceas", "ora"))
print(a.index("ra"))
print(a.isalnum())
print(a.isalpha())
print(a.isascii())
print(a.isdecimal())
print(a.isdigit())
print(a.isidentifier())
print(a.islower())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.istitle())
print(a.isupper())
print(a.join("ceas"))
print(a.ljust(2))
print(a.lower())
print(a.lstrip())
print(a.partition("ceas, orologiu"))
print(a.replace("ceas", "orologiu"))
print(a.rfind("orologiu"))
print(a.rindex("ceas"))
print(a.partition("ceas"))
print(a.split())
print(a.rstrip())
print(a.splitlines())
print(a.startswith("o"))
print(a.startswith("ce"))
print(a.strip())
print(a.swapcase())

