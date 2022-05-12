from 2 February.Decorator import my_unit_test

@my_unit_test
def test1(a):
    assert sum([1, 12], a == 15)

test1(15)
my_unit_test(test1)(2)

