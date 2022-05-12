# # Functia integreaza o structura de cod care are ca scop furnizarea de output.
import psutil


def hello(test, x=1, y=2):
    print(test, x, y)


hello(10, 12, 5)


def magazin(faina, ulei=5, masline=10):
    print(faina, ulei, masline)


magazin(4, 6, 12)


def timp(ceas, pret=100, locatie=25):
    print(ceas, pret, locatie)


timp(5, 120, 30)


def destinatie(masina, haine=300, mancare=200):
    print(masina, haine, mancare)


destinatie(20, 250, 150)


def tehnologie(bratara=20, laptop=30, mouse=40, tastatura=50, telefon=60, tableta=70, router=50):  # elemente cu valori
    print(bratara, laptop, mouse, tastatura, telefon, tableta, router)  # elementele


tehnologie(800, 3000, 40, 2000, 602, 1000, 504)  # valori


def stiri(pozitive=100, negative=0, neutre=50):
    print(pozitive, negative, neutre)


stiri()


def youtube_min(clip_IT, video_amuzant, peisaj_frumos, muzica_buna):
    print(clip_IT, video_amuzant, peisaj_frumos, muzica_buna)


youtube_min(102, 40, 50, 100)


def youtube_min(clip_IT=100, video_amuzant=20, peisaj_frumos=30, muzica_buna=50, stiri=30, youtube="min"):
    print(clip_IT, video_amuzant, peisaj_frumos, muzica_buna, stiri, " ", end=youtube)


youtube_min()

print("")


def google(gmail, stiri, drive, meteo, jocuri, meet, aplicatii, extensii):
    print(gmail, stiri, drive, meteo, jocuri, meet, aplicatii, extensii)


google(1000, 125, 225, 330, 253, 756, 195, 72)


def twitter(*postarea):
    print(f"Twitter :Platforma sociala care include {postarea}")
    print(f"Twitter :Platforma sociala care include {postarea[0]}")
    print(f"Twitter :Platforma sociala care include {postarea[1]}")
    print(f"Twitter :Platforma sociala care include {postarea[2]}")
    print(f"Twitter :Platforma sociala care include {postarea[3]}")


twitter("stiri", "inovatii", "opinii", "pareri", "vieti", "frumuseti")


def hub_inovatii(*retele_sociale):  # *Se pot declara nenumarate argumente
    print(f"Acestea sunt ultimele inovatii in materie de retele sociale: {retele_sociale}")
    print(f"O retea sociala recent aparuta este: {retele_sociale[0]}")
    print(f"O retea sociala recent aparuta este: {retele_sociale[1]}")
    print(f"O retea sociala recent aparuta este: {retele_sociale[2]}")
    print(f"O retea sociala recent aparuta este: {retele_sociale[3]}")


hub_inovatii("TikTok", "Instagram", "Snapchat", "Metaverse")


# @mydecorator
def hub_inovatii(
        **retele_sociale):  # *Se pot declara nenumarate argumente,** Se stie exact care este numele, care este acoperirea.
    print(f"Acestea sunt ultimele inovatii in materie de retele sociale: {retele_sociale['nume_1']}")
    print(f"O retea sociala recent aparuta este: {retele_sociale['acoperire_1']}")
    print(f"O retea sociala recent aparuta este: {retele_sociale['nume_2']}")
    print(f"O retea sociala recent aparuta este: {retele_sociale['acoperire_1']}")
    print(f"O retea sociala recent aparuta este: {retele_sociale['nume_3']}")
    print(f"O retea sociala recent aparuta este: {retele_sociale['acoperire_1']}")


hub_inovatii(nume_1="TikTok", acoperire_1="Tot globul aproximativ", nume_2="Instagram",
             acoperire_2="Tot globul aproximativ", nume_3="Snapchat", acoperire_3="Tot globul aproximativ",
             nume_4="Metaverse", acoperire_4="Tot globul aproximativ")


def get_virtual_memory():
    print(psutil.virtual_memory().percent)


get_virtual_memory()


def get_virtual_memory_2():
    return psutil.virtual_memory().percent


a = get_virtual_memory_2()
print(a)


# Partea de testare:
def display_test_logs(msg):
    def logger():
        print(f"Logging memory data.{get_virtual_memory_2()}{msg}")

        def test():
            print("Hello")

        test()

    logger()


display_test_logs("thumbs up")


def display_test_logger(msg):
    def logger():
        print(f"Te-ai logat.{get_virtual_memory()}{msg}")

        def test():
            print("Test")

        test()

    logger()


display_test_logs("Buna !")


def get_get_virtual_memory():
    print(psutil.virtual_memory().percent)


get_virtual_memory()


def display_test_logs(msg):
    def logger():
        print(f'Bine ati venit! ')

        def test():
            print(f'Test efectuat cu succes ! {get_virtual_memory()}{msg}')

        test()

    logger()


display_test_logs("La revedere !")



def display_test_logs_2(msg):
    threshold = 90

    def logger():
        print(treshold)

    return logger


display_test_logs_2()()


def display_test_logs(msg):
    treshold= 5
    def logger():
        print(treshold)
    return logger

display_test_logs()()

class Calculator:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def sum(self, a, b):
        print(self._a + self._b)

    def dif(self, a, b):
        print(self._a - self._b)

    def inmultire(self, a, b):
        print(self._a * self._b)

    @staticmethod
    def impartire(a, b):
        return a / b


Laptop = Calculator(1, 2)
print(Laptop.sum(1, 2))
print(Laptop.dif(1, 2))
print(Laptop.inmultire(1, 2))
print(Laptop.impartire(1, 2))


def myfunc(a, b):
    print(a + b)


myfunc(1, 2)


def myfunc(x, y):
    return x + y


suma = myfunc(1, 2)
print(suma)


def even_check(number):
    return number % 2 == 0

even_check(20)

