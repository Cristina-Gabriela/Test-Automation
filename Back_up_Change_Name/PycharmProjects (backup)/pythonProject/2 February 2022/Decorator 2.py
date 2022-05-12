def my_unit_test(func):
    def wrapper(a):
        print(f"My unit test started for {a}")
        func(a)
        print("Unit test is finished.")

    return wrapper

@my_unit_test
def test1(a):
    assert sum([1, 12], a == 15)

test1(15)

my_unit_test(test1)(2)









