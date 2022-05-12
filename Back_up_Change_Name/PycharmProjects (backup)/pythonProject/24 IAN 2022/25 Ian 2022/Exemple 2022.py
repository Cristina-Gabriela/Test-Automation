
astr = "Bob"
try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    istr = -1
print("Done", istr)

rawster = input("enter a number:")
try :
    ival = int(rawster)
except:
    ival = -1
if ival > 0:
    print("Nice work")
else:
    print("Not a number")


def thing():
    print("Hello")
    print("Fun")
thing()
print("Zip")
thing()


def ceas():
    print("Ora")
    print("Vacanta")
ceas()
ceas()
ceas()
ceas()
ceas()
ceas()
ceas()
ceas()
ceas()
ceas()
ceas()

#Functions: Store and reuse steps:
# def statement = remember a code, stock and reuse the steps.
# invoca un lucru((thing: denumit cum vrem noi) si extinde programul in Python cu def statement
#Al doiles lucru (thing) reutilizeaza datele de la primul si il afiseaza.

def Automatizare():
    print("Automatizarea taskurilor ")
Automatizare()
Automatizare()
Automatizare()
Automatizare()

def ROBOTEL():
    print("E soare in Dubai")
ROBOTEL()
ROBOTEL()
ROBOTEL()
ROBOTEL()
ROBOTEL()
ROBOTEL()
ROBOTEL()
ROBOTEL()
ROBOTEL()


print(1+2*float(3)/4-5)

def Loc_de_munca():
    print("Doresc sa am un loc de munca foarte bine platit")
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()
Loc_de_munca()

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')

greet('en')
greet('fr')
greet('es')

def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('en'), 'Gleen')
print(greet('fr'), 'Sally')
print(greet('es'), 'Michael')