# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg
#
#     return total
#
# print(multiply(1, 3, 5))
# print(multiply(-1))

# def multiply(*fdfd):
#     print(fdfd)
#
# multiply(1,3,5,5,4,7,895,54,54,21)


# def register(*persons):
#     print(persons)


# register("A", "D", "Ds", "fdn", "fndlw", "dfjsk")

# def salaries(*test):
#     print(test)

# salaries("4000 EURO", "2 EURO", "16000 EURO", "32000 EURO", "etc.")

# def salaries(*test):
#     print(test)
#     total = 1
#     for i in test:
#         total = total * i
#     return total


# salaries("4000 EURO", "2 EURO", "16000 EURO", "32000 EURO", "etc.")
# print(multiply(4000, 2, 16000, 32000))
# print(multiply(-1))


# def add(x, y):
#     return x + y


# nums = [10, 3]
# print(add(*nums))

# def apply(*args, operator):
#     if operator == "*":
#         return multiply(args)
#     elif operator == "+":
#         return sum(args)
#     else:
#         return "No valid operator provided to apply()."
#
#
# print(apply(1, 3, 6, 7, operator="+"))


# def sum(*args, operator):
#     if operator == "*":
#         return multiply(args)
#     elif operator == "+":
#         return sum(args)
#     else:
#         return "Without operators."
#
#
# print(sum(2, 5, 6, 8, 92, 10, 124, operator="*"))
#
# def operation(*args):
#     print(args)
#     total = 1
#     for i in args:
#         total = total * i
#     return total


# def operation(*args, operator):
#     print(*args)
#     if operator == '+':
#         return sum(args)
#     else:
#         return 'Nothing'
#
#
# print(operation(100, 9, 5, 2, operator='+'))

#
# def life_expectancy(**kwargs):
#     print(kwargs)
#
#
# life_expectancy(name="people x", age=101)


# def life_expectancy(name, age):
#     print(name, age)
#
#
# details = {"name": "people x", "age": 101}
# life_expectancy(**details)
#


# def life_expectancy(*kwargs):
#     print(kwargs)
#
#
# details = {"name": "people x", "age": 101}
# life_expectancy(*details)
# life_expectancy(details)


# def life(**kwargs):
#     print(kwargs)


# def life_expectancy(**kwargs):
#     print(kwargs)
#     life(**kwargs)
#     for arg, value in kwargs.items():
#         print(f"{arg}:{value}")
#
#
# life_expectancy(name="people x", age=101)


# def life(**param):
#     print(param)

# life(an_p_1=100, an_p_2=101, an_p_3=102, an_p_4=103, an_p_5=104)

#
# def both(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# both(1, 2, 3, 5563, 787, 121, 488, 52, name="DSBJBDS", age="4", price="54545265")
#
#
# def myfunction(*kwargs):
#     print(kwargs)
#
#
# myfunction(*"A", *"ncdjkscd", *"dsnlkncdj")
# myfunction(*"Todayisabigday", *"dskjndckj")

#
# def Automation(*parameter, **kwargs):
#     print(parameter)
#     print(kwargs)
#
#
# Automation("Clock")
# Automation("Time", "Social Media", "Time")

student = {"name": "Edi", "product_price": (10, 20, 30, 45, 56, 789, 121212, 120, 4)}


def average(product_price):
    return sum(product_price) / len(product_price)


def average(sequence):
    return sum(sequence) / len(sequence)


# 10 + 20 + 30 + 45 + 56 + 789 + 121212 + 120 + 4 / 9

print(average(student["product_price"]))  # Question: Hei Student, what is your average product_price ?


# database = {"name": "BIGDATA", "price_server_number": (12, 23, 56, 78, 56, 78, 91, 11, 111, 263)}

# def average_price_server_number(server_number):
#     return sum(server_number) / len(server_number)

# print(average_price_server_number(database["price_server_number"]))
class Student:  # definition of something
    def __init__(self, name, grades):  # A function inside a class is call a method

        self.name = name  # take the value of the name variable.
        self.name = "Rolf"  # . =  Accesing the name property inside of self and then you give a variable name.
        #  Creating a thing from a class
        #  This self name contains a self property, Python will give back you self.
        self.grades = (90, 23, 56, 8, 5, 56)

    def average(self):
        return sum(self.grades / len(self.grades))

    student = Student("Bob", (90, 23, 56, 8, 5, 56))
    student_1 = Student("Sfcdfd", (90, 23, 56, 8, 5, 56))
    student_2 = Student("A", (95, 45, 478, 12, 7))
    student_3 = Student("B", (978, 21, 45657, 12, 4))
    student_4 = Student("C", (97874, 121, 4587,))
    # We use the class to called an object in Python that behaves what the class defines.
    # () You will call the class and then automatically call the method __init__ and it will create an empty thing
    # called self and you will be able to modify the name property inside self and give the value Rolf.
    # student become a name for self thing we created. That thing become an object.
    # It can be different --- self.name = "Rolf". Overwrite here if "Bob" appears.

    print(student.name)  # So, printing student.name =  And what are you doing is to access the name property of your student variable
    # which is self created earlier and give you ROLF.
    print(Student.average(student))  # Calling the average methode inside the student class and the self parameter is going to take the value
    # of the student variable which has the object that has created earlier in self.grades.

    print(student.name)
    print(student.grades)
    print(student_1.average())
    print(student_2.average())
    print(student_3.average())
    print(student_4.average())

# 1. You call a class
# 2. The init class run
# 3. When you get back is the object you created.


# Simplify life greatly
