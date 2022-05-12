def test(func, arg):
  return func(func(arg))
def mult(x):
  return x * x
print(test(mult, 2))

def test(func, arg):
    return func(func(arg))
def mult(x):
    return x * x
print(test(mult, 2))

def pure_function(x, y):
  temp = x + 2*y
  return temp / (2*x + y)

