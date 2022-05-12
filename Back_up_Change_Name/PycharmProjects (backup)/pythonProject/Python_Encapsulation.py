class Encapsulation:
    def set_public(self):
        print("I am visible.")

    def _set_protected(self):
        print("I am protected.")

    def __set_private(self):
        print("I am not visible outside the class.")
    def get(self):
        self.__set_private()
    def _gets(self):
        self._set_protected()
    def gety(self):
        self.__set_private()
x = Encapsulation()

x.set_public()
x._set_protected()

x._gets()
x.gety()




# x.get()
# x._set_protected()
# x.get()

# x.__set_private()

# x.set_public()
