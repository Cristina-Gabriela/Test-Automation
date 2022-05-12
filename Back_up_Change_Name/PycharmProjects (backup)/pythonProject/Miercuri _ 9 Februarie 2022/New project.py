# Abstractizare :
from abc import ABC, abstractmethod


# Abstract Base Class

class TestModel(ABC):
    @abstractmethod
    def set_up(self):
        pass

    @abstractmethod
    def execute(self):
        raise NotImplemented  # sa marcam o metoda ca fiind fara implementare.

    @abstractmethod
    def tear_down(self):
        raise NotImplemented


# guide line
class Test1(TestModel):
    def set_up(self):
        print("Implement the test1 !")

    def execute(self):
        print("Execute the test1.")

    def tear_down(self):
        print("Shut down the test1.")


# cream obiect:

if __name__ == '__main__':  # foarte important
    test1 = Test1()  # constructor
    test1.set_up()
    test1.execute()
    test1.tear_down()

print(" ")
class Test2(TestModel):
    def set_up(self):
        print("Implement the test2 !")

    def execute(self):
        print("Execute the test2.")

    def tear_down(self):
        print("Shut down the test2.")

if __name__ == '__main__':  # foarte important
    test2 = Test2()
    test2.set_up()
    test2.execute()
    test2.tear_down()

if __name__ == '__main__':  # foarte important
    test1 = Test1()
    test2 = Test2()
    # polimorfism -
    for test in test1, test2:
        test.set_up()
        test.execute()
        test.tear_down()

