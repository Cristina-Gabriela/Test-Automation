class Base:
    def __init__(self, driver):
        self._browser = driver  # constructor

    def open_browser(self, url):  # metode setate in interiorul clasei
        print(f"Open{self._browser} browser for {url}")

    @staticmethod   # poti sa apelezi metoda adnotata cu @staticmethod, fara sa am un obiect de tipul respectiv instantiat
    def quit_browser():
        print("We will close the browser! ")


chrome = Base("chrome driver")  # Initializare obiect
chrome.open_browser('https://www.google.com')  # Apelare metoda
Base.quit_browser()
chrome.quit_browser()


class Child:
    pass


print(" ")


class Base:
    def __init__(self, driver):
        self._browser = driver  # constructor

    def open_browser(self, url):  # metode setate in interiorul clasei
        print(f"Open{self._browser} browser for {url}")

    @staticmethod
    def quit_browser():
        print("We will close the browser! ")


class Child(Base):
    def set_up(self):
        print("Set your test environment")
        self.open_browser("www.facebook.com")

    @staticmethod
    def run_steps():
        print("Steps to be added later on.")

    def tear_down(self):
        print("Quit test !")
        self.quit_browser()


class FirstTest(Child):
    def run_steps(self):
        print("Print step1, step2, step3")


class SecondTest(Child):  # comportament polimorfic
    def run_steps(self):
        print("Click on login button and enter the invalid credentials.")


if __name__ == "__main__":  # S-a generat un if statement automat., # Le-am grupat. # Sa nu mai repetam in tot codul. # Marcam tot ce trebuie sa rulam in "Inheritance".
    chrome = Base("chrome driver")  # Initializare obiect

    chrome.open_browser('https://www.google.com')  # Apelare metoda

    chrome.quit_browser()

    child = Child("Firefox")
    child.set_up()
    child.tear_down()
    child.run_steps()

    test1 = FirstTest("Safari")
    test1.run_steps()

    test2 = SecondTest("Mozilla")
    test2.run_steps()
    # comportament polimorf.

    print(SecondTest.mro())
