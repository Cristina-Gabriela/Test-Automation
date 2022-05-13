class Encapsulation:
    def set_public(self):
        print("I am visible on the entire project.")

    def _set_protected(self):
        print("I am visible by child.")

    def __set_private(self):
        print("I am not visible outside the class.")

    def get(self):
        self.__set_private()

class Child(Encapsulation):
    def test(self):
        self.set_public()
        self._set_protected()


x = Encapsulation()
x._set_protected()
#x.__set_private()
x.get()
x.set_public()

y = Child()
y.test()







