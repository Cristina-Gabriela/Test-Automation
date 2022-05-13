def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

print(multiply(1, 3, 5))
print(multiply(-1))

def multiply(*fdfd):
    print(fdfd)

multiply(1,3,5,5,4,7,895,54,54,21)


def register(*persons):
    print(persons)


register("A", "D", "Ds", "fdn", "fndlw", "dfjsk")

def salaries(*test):
    print(test)

salaries("4000 EURO", "2 EURO", "16000 EURO", "32000 EURO", "etc.")

def salaries(*test):
    print(test)
    total = 1
    for i in test:
        total = total * i
    return total


salaries("4000 EURO", "2 EURO", "16000 EURO", "32000 EURO", "etc.")
print(multiply(4000, 2, 16000, 32000))
print(multiply(-1))


def add(x, y):
    return x + y


nums = [10, 3]
print(add(*nums))

def apply(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."


print(apply(1, 3, 6, 7, operator="+"))


def sum(*args, operator):
    if operator == "*":
        return multiply(args)
    elif operator == "+":
        return sum(args)
    else:
        return "Without operators."


print(sum(2, 5, 6, 8, 92, 10, 124, operator="*"))

def operation(*args):
    print(args)
    total = 1
    for i in args:
        total = total * i
    return total


def operation(*args, operator):
    print(*args)
    if operator == '+':
        return sum(args)
    else:
        return 'Nothing'


print(operation(100, 9, 5, 2, operator='+'))


def life_expectancy(**kwargs):
    print(kwargs)


life_expectancy(name="people x", age=101)


def life_expectancy(name, age):
    print(name, age)


details = {"name": "people x", "age": 101}
life_expectancy(**details)



def life_expectancy(*kwargs):
    print(kwargs)


details = {"name": "people x", "age": 101}
life_expectancy(*details)
life_expectancy(details)


def life(**kwargs):
    print(kwargs)


def life_expectancy(**kwargs):
    print(kwargs)
    life(**kwargs)
    for arg, value in kwargs.items():
        print(f"{arg}:{value}")


life_expectancy(name="people x", age=101)


def life(**param):
    print(param)

life(an_p_1=100, an_p_2=101, an_p_3=102, an_p_4=103, an_p_5=104)


def both(*args, **kwargs):
    print(args)
    print(kwargs)


both(1, 2, 3, 5563, 787, 121, 488, 52, name="DSBJBDS", age="4", price="54545265")


def myfunction(*kwargs):
    print(kwargs)


myfunction(*"A", *"ncdjkscd", *"dsnlkncdj")
myfunction(*"Todayisabigday", *"dskjndckj")


def Automation(*parameter, **kwargs):
    print(parameter)
    print(kwargs)


Automation("Clock")
Automation("Time", "Social Media", "Time")
student = {"name": "Edi", "product_price": (10, 20, 30, 45, 56, 789, 121212, 120, 4)}


def average(product_price):
    return sum(product_price) / len(product_price)


def average(sequence):
    return sum(sequence) / len(sequence)

print(average(student["product_price"]))


class Student:
    def __init__(self, name, grades):

        self.name = name
        self.name = "Rolf"
        self.grades = (90, 23, 56, 8, 5, 56)

    def average(self):
        return sum(self.grades) / len(self.grades)

    student = Student("Bob", (90, 23, 56, 8, 5, 56))
    student_1 = Student("Sfcdfd", (90, 23, 56, 8, 5, 56))
    student_2 = Student("A", (95, 45, 478, 12, 7))
    student_3 = Student("B", (978, 21, 45657, 12, 4))
    student_4 = Student("C", (97874, 121, 4587,))


    print(student.name)
    print(student.average(student))
    print(student.name)
    print(student.grades)
    print(student_1.average())
    print(student_2.average())
    print(student_3.average())
    print(student_4.average())


