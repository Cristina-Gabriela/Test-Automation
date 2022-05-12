def add(x, y):
    return x + y


def do_twice(func, x, y):
    return func(func(x, y), func(x, y))
a = 5
b = 10

print(do_twice(add, a, b))


def add(a, b):
    return a + b

def do_twice(func, a, b):
    return func(func(a, b), func(a, b))
    a = 2
    b = 3
print(do_twice(add, a, b))



import random
for i in range(10):
    value= random.randint(1,10)
    print(value)


def print_nums(x):

  for i in range(x):

    print(i)

    return

print_nums(10)











