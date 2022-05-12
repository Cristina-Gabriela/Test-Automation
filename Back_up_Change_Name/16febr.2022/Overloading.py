from overload import overload


class TestCase:
    @overload
    def run(self, a):
        print("This is " + a)

    @run.add
    def run(self, a, b):
        print("This is " + a + b)

    @run.add
    def run(self, a, b, c):
        print("This is " + a + b + c)

testcase = TestCase()
testcase.run("a")
testcase.run("ab ","cd")
testcase.run("abc ","def ","ghi")




