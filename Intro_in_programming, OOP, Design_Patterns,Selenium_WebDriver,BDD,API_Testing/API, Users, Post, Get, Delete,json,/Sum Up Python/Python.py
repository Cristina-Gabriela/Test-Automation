x = 15
price = 9.99

discount = 0.2
result = price * (1 - discount)
print(result)

name = "Bob"
s = "XYZ"
x = "Abc"
greeting = f"Hello, {name}"
print(greeting)

S_greeting = f"Hello, {s}"
print(S_greeting)

x_greeting = f"Hello, {x}"
print(x_greeting)

with_name_one = greeting.format(name)
with_name_two = greeting.format(s)
with_name_3 = greeting.format(x)

print(with_name_one)
print(with_name_two)
print(with_name_3)

phrase = "Hello, {}. Today is {}."

x = phrase.format("D", "G")
print(x)

dictionary = "Today is {} and tomorrow will be {}."

a = dictionary.format("9 Apr", "10 Apr")

print(a)

x_input = input("There is:")
total = int(x_input)
sq = total / 10.2
print(f"{total} xyz {total:.2f} km.")
print(f"{sq} xyz {sq:.2f} km.")

user_age = input("Enter your age:")
years = int(user_age)
months = years * 12
print(f"Your age is: {years} years, is equal to {months} months.")

l = ["Bob", "Rolf", "A"]
AB = ["Bob", "Rolf", "A"]
t = ("Bob", "Rolf", "A")

# sets
s = {"Bob", "Rolf", "A"}

print(l[2])
l[0] = "Smith"
print(l)

l.append("Smith")
print(l)

AB.remove("Bob")
print(AB)

AB.append("Tania")
print(AB)

AB.clear()
print(AB)

friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)
print(local_friends)

local_friends = abroad.difference(friends)
print(local_friends)

friends = local_friends.union(abroad)
print(friends)

friends = local_friends.union(friends)
print(friends)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)

print(10 == 10)
print(5 > 5)
print(10 != 10)

friends = ["Rolf", "Bob"]
abroad = ["Rolf", "Bob"]

print(friends == abroad)
print(friends is abroad)
print(friends is friends)

day_of_week = input("What day of the week is it today?").lower()
print(day_of_week == "Monday")

if day_of_week == "MONDAY":
    print("Have a good start to your week!")
elif day_of_week == "Tuesday":
    print("It's Tuesday.")
else:
    print("Another day !")
if day_of_week != "MONDAY":
    print("Full speed ahead")

print("This always runs.")

x = ["56", "89", "8546", "598", "1235"]
y = ["5656", "897", "8975", "45610", "1254"]

print(x == y)

if x == y:
    print("True")
else:
    print("Not True")

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

print(art == science)

if art == science:
    print("An exercise")
elif art != science:
    print("Another exercise")
else:
    print("Exception")

art = {"Bob", "Jen", "Rolf", "Charlie"}
user_movie = input("Enter one name")
print(user_movie in art)

if user_movie in art:
    print("Jen")
else:
    print("12")

exercise = {"Happy", "Sad", "Angry", "Peaceful"}
mood_person = input("input the mood")
print(mood_person in exercise)

if mood_person == exercise:
    print("Exactly")
else:
    print("Not the real mood")


exercise = {"Happy", "Sad", "Angry", "Peaceful"}
mood_person = input("input the mood")

if mood_person in exercise:
    print(f"The person was {mood_person} too!")
else:
    print("Nobody had this mood")

number = 10
user_to_guess = input("Enter a number that you want (Y/n): ")

print(user_to_guess == 10)

while user_to_guess != "n":

    # if user_to_guess == "y":
    user_to_guess = int(input("Enter a number: "))
    if user_to_guess == number:
        print('Right')
    else:
        print("No right")

number = 7
user_input = input("Enter a letter if you would like to play: (yes/non)")

# while True:
while user_input != "n":
    user_number = int(input("Guess the number: "))
    if user_input == "y":
        user_number = int(input("Guess the number: "))
        if user_number == number:
            print("OK")
        else:
            print("No")



price_product = 10
user_budget = input("Please enter the price of the product:")

if user_budget == 10:
    print("The sum is correct !")

price_product_1 = "10"
user_budget = input("Please enter the price of the product:")
# print("The price of the product is 10")

if user_budget == price_product_1:
    print("The price of the product is 10")

if user_budget != price_product_1:
    print("The price of the product has changed.")

print("The End !")

price_product_1 = "10"
price_product_2 = "20"
user_budget = input("Please enter the price of the product:").lower()
# print("The price of the product is 10")

if user_budget == price_product_1:
    print("The price of the product is 10")
elif user_budget == price_product_2:
    print("The price of this product is 20")
else:
    print("The price of the product has changed.")

print("The End !")

x = "monday"
y = "tuesday"
day_of_the_week = input("What is the day of the week? ").lower()

if day_of_the_week == x:
    print("The day of the week is Monday. Have a nice week.")
elif day_of_the_week == y:
    print("This day is Tuesday. Good luck !")
else:
    print("This is another day in the week. Enjoy !")

print("Finish")

# while user_budget == price_product:
#     print("On the way !")

cost_1 = "2000 euro"
cost_2 = "4000 euro"
payment_card = input("This is your bill. Please enter the sum: ").lower()

if cost_1 in payment_card:
    print("The operation 1 was successfully")
elif cost_2 in payment_card:
    print("The operation 2 was successfully")
else:
    print("It is an error.Try again.")

print("Finish")


price = 10
budget_client = input("Please enter 'yes' if you want to continue this operation.")

while budget_client != "non":
    if budget_client == "yes":
        client = int(input("Enter the price of the product."))
        while client != 10:
            if client == price:
                print("You can retrieve your product.")
            # elif abs(price - budget_client) == 0.1:
            #     print("The sum is too little, you can retrieve the product.")
            else:
                print("You are not able to retrieve the product.")
                break
print("Finish")


add_sum = {"10", "25", "56", "89", "152", "78"}
CARD = input("Verify if the sum added in your valet is correct: ")

if CARD in add_sum:
    print(f"The sum {CARD} was validated.")
else:
    print("The sum added in your valet is incorrect.")


decentralized_finance = {"ethereum", "smart contract", "stablecoin", "Bitcoin", "blockchain"}
key_word = input("Verify if your subject is on the list")


if key_word in decentralized_finance:
    print(f"The {key_word} was verified and it exist.")
else:
    print("The Decentralized finance not support your key_word")


PIN = 8524
ATM = input("Press (yes/non) if you want to continue.")

while ATM == "yes":
    if ATM == 'yes':
        print("You can continue to verify the key_word. Welcome to Next step.")
        person = int(input("Enter your PIN: "))
        while PIN == 8524:
            if person == PIN:
                print('It is correct.')
            else:
                print('Try again')
            break
else:
    print("You can try again.")


decentralized_finance = {"ethereum", "smart contract", "stablecoin", "Bitcoin", "blockchain"}
key_word = input("Verify if your subject is on the list")

if key_word in decentralized_finance:
    print(f"The {key_word} was verified and it exist.")
else:
    print("The Decentralized finance not support your key_word")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)

user_input = input("Enter your choice: ")
if user_input == "a":
    print("Add")
elif user_input == "q":
    print("Quit")


# List comprehension :

numbers = [10, 56, 98, 2546]
double_numbers = [i ** 2 for i in numbers]
print(double_numbers)

for i in numbers:
    double_numbers.append(i ** 2)
print(double_numbers)

cod = [2, 89, 152, 78, 52, 89, 52, 56, 786, 123, 16, 8]
cod_plus_10 = [i + 10 for i in cod]
print(cod_plus_10)


for i in cod:
    cod_plus_10.append(i+10)

print(cod_plus_10)

name = ["Ana ", "Maria ", "Evelina ", "Alin ", "George ", "Oliver ", "Christoffer "]
name_multiply_5 = [i * 5 for i in name]
print(name_multiply_5)

friends = ["Ana ", "Maria ", "Evelina ", "Alin ","Felicia", "George ", "Oliver ", "Christoffer ", "Felix", "Edi"]
starts_s = []


for i in friends:
    if i.startswith("A"):
        starts_s.append(i)
    if i.startswith("F"):
        starts_s.append(i)
    if i.startswith("E"):
        starts_s.append(i)

print(starts_s)


friends = ["Ana ", "Maria ", "Evelina ", "Alin ", "Felicia", "George ", "Oliver ", "Christoffer ", "Felix", "Edi"]
x = [i for i in friends if i.startswith("F")]
print(x)
print("friends: ", id(friends), "x: ", id(x))


price = ["l10", "l25", "l56", "l89", "a123", "a123", "k7892", "u12456589", "u18952", "t14123"]
start_with = [i for i in price if i.startswith("l")]
print(start_with)
print(price[0] is start_with[0])
print("price: ", id(price), "start_with: ", id(start_with))

# Dictionaries:

price_vegetables = {"onion": 3, "persil": 1, "tomato": 4.5 }
price_vegetables["Pepper"] = 9
print(price_vegetables["onion"])
print(price_vegetables)

price = [
    {"vegetables": "onion", "price": "3"},
    {"vegetables": "persil", "price": "1"},
    {"vegetables": "tomato", "price": "4.5"},
    {"vegetables": "pepper", "price": "9"},

]

print(price)
print(price[1])
print(price[2])
print(price[0])
print(price[1]["vegetables"])
print(price[2]["vegetables"])
print(price[3]["vegetables"])

price_vegetables = {"onion": 3, "persil": 1, "tomato": 4.5}

for i in price_vegetables:
    print(price_vegetables)
    print(f"{i}:{price_vegetables[i]}")

for i, v in price_vegetables.items():
    print(price_vegetables)
    print(f"{i}:{v}")

technology = [
    {"mouse": "one"},
    {"keyboard": "one"},
    {"desktop": "two"},
    {"cable": "three"},
]
print(technology)
print(technology[0])
print(technology[1])
print(technology[2])
print(technology[3])

# for i in technology:
#     print(f"{i}:{technology[i]}")

for i, a in technology:
    print(f"{i}:{a}")

t = 5, 11
x, y = t
print(x, y)

dictionary = 10, 12
x, y = dictionary
print(x, y)

laptop = 100, 121
key, mouse = laptop
print(key, mouse)

dictionary = {"S": 100, "A": 56, "D": 89}
print(list(dictionary.items()))
for x, y in dictionary.items():
    print(f"{x}:{y}")

dictionary = {"A": 5, "B": 56, "R": 89}
print(list(dictionary.items()))
for i, a in dictionary.items():
    print(f"{i}:{a}")

Python = {"cod": 23, "s": 56, "int": 568}
print(list(Python.items()))
for k, v in Python.items():
   print(f"{k},{v}")

for x in Python.items():
    print(x)

# json = {("Name": "Felix", "Age": 25, "Profession": "IT")}
json = [("Felix", 25, "IT at Microsoft"), ("Oliver", 30, "Software Developer at Google"),
        ("Christoffer", 20, "Hacker at Facebook ")]
for key, value1, value2 in json:
    print(key, value1, value2)

for x in json:
    print(x)

for key, value1, value2 in json:
    print(f"{key} - {value1} - {value2}")

price = [("fly dubai", "15 Euro", "4 person", "window"), ("blueair", "20 Euro", "14 person", "window"),
         ("wizzAir", "10 Euro",
          "2 person", "window")]



for key, v1, v2, v3 in price:
    print(f" Name: {key}, price: {v1}, number_of_persons: {v2}, seat: {v3} ")

for key, v1, v2, v3 in price:
    print(f"{key} : {v1}, {v2}, {v3}")

price = {"fly dubai": "15 Euro, 4 person, window"}
for x in price.items():
    print(x)

price = ("fly dubai", "15 Euro", "4 person", "window")

Company, _, number_persons, seats = price
C, _, n, s = price
print(C, _, n, s)

flower, *apple, grass = [1,2,85,92,5754]
print(flower)
print(*apple)
print(grass)

def Automation():
    print("Automation")

Automation()

def user_age_in_seconds():
    user_age = int(input("Enter your age : "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in second is {age_seconds}.")


user_age_in_seconds()


def name():
    x = int(input("Enter your number: "))
    y = x ** 526
    print(f"Your number is {x}.")


name()

friend = []

def add_friend():
    friend.append("Ana, A., As., Shj. ")

add_friend()
add_friend()

print(friend)

list = []


def add_fruits():
    list.append("a")


add_fruits()
add_fruits()
add_fruits()

print(list)

def add(x, y):
    result = x + y
    print(result)


add(10, 25)


def add_cash(number):
    print(f"The cash recently added is {number}. ")

add_cash(+568546897489548794)

def another_function(benefits, lifestyle):
    print(f"The enterprises have {benefits} of benefits and a good {lifestyle}.")
    print(f"The enterprises have {benefits} of benefits and a good {lifestyle}.")

another_function("a lot", "lifestyle for the employees")
another_function(benefits="a lot", lifestyle="lifestyle for the employees")

print("Welcome in your wallet :) ")


def power_of_buying():
    power = int(input("Please enter your power of buying: "))
    power_min = power * 12
    print(f"Your power of buying for one year is {power_min} It can be more each year for a better life. ")


power_of_buying()
print("Good bye ! ")
print("Welcome in your wallet :")
buy_person_x = ["A", "B", "C", "F"]


def add_power_of_buying():
    power = input("Please enter your power of buying: ")
    power_min = [power] + buy_person_x
    print(f"Your power of buying for one year is {power_min} It can be more each year for a better life. ")


add_power_of_buying()
print("Good bye ! ")

wallet = [100, 2000, 52, 986, 7854562, 7, 23, 8945123214567]
secret_number = [1245]


def add_in_wallet():
    first_add = input(f'Please enter in wallet the sum:')
    second_add = input(f'Please enter your PIN to validate the transaction:')
    # assert first_add in wallet
    # assert second_add in secret_number

    if first_add in wallet:
        # assert first_add is second_add
        print('It is correct')

    if second_add in secret_number:
        print('True PIN')


add_in_wallet()

say_hello()


def say_hello():
    print("Hello")


add_sum = []
def sum():
    add_sum.append("100000000000000000000000000")


sum()
sum()

print(add_sum)

technology = []


def inovtechtest():
    technology.append("Laptop")
    technology.append("Mouse")
    technology.append("etc")


inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()
inovtechtest()

print(technology)


def add(x, y, a, b, f, g):
    result = x + y + b + f + g + a
    print(result)


add(132, 154, 45, 12, 45, 825)

def devide(devidend, divisor):
    if divisor != 0:
        print(devidend / divisor)
    else:
        print("You fool! ")


devide(15, 0)


def divide(param_1, param_2):
    all = param_1 / param_2
    if all == 5:
        print("All it's ok !")
    else:
        print("Not, you can try again !")
    assert all == 5
    print("Validation !")
    assert all != 10
    print("Also validated !")


divide(25, 5)


def divide(param_1, param_2):
    all = param_1 / param_2
    if all == 5:
        return ("All it's ok !")
    else:
        return ("Not, you can try again !")
    assert all == 5
    print("Validation !")
    assert all != 10
    print("Also validated !")


x = divide(25, 5)
print(x)
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Felix")
say_hello("S")
say_hello("Eva")

def buy(Param1, Param2):
    print(f'Something to buy: {Param1, Param2}')


buy("Laptop", "Mobile Phone")
buy("Mobile Phone", "Car")
buy("Car", "Laptop")

default_y = 10


def add(x, y=default_y):
    print(x + y)


add(10)
# add(10, 18)

default_cod_job = 21545


def set_job(default_cod_job, cod_job_changed):
    print(
        f"This is the first cod of Software Engineer position {default_cod_job}. And today, the cod was changed into: {cod_job_changed}.")


set_job(default_cod_job, 15645)
set_job(default_cod_job, 898989)
set_job(default_cod_job, 454)
set_job(default_cod_job, 5648)

default_salary = 5000000000


def add_salary(default_salary, increased_salary):
    print(f"This was your last salary {default_salary} and now, your salary is: {increased_salary}")



add_salary(default_salary, increased_salary=8000000000)
add_salary(default_salary, increased_salary=10000000000)
add_salary(default_salary, increased_salary=11000000000)


a = 10
b = 20


def my_function(x, y):
    return a * b


x = my_function(10, 20)
print(x)
print(my_function(10, 20))


def add(x, y):
    return x + y

print(add(5, 7))


 # the same :
add = lambda x, y: x + y

print(add)

(lambda x, y: x + y)(5, 7)

print(add(5, 7))

print(lambda x, y: x + y)(5,7)


def double(x):
    return x * 2


sequence = [1, 2, 3, 5, 9]
doubled = [x * 2 for x in sequence]
doubled = [double(x) for x in sequence]
doubled = map(double, sequence)


def double(x):
    return x * 2


sequence = [1, 2, 3, 5, 9]
doubled = [x * 2 for x in sequence]
doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled = list(map(lambda x: x * 2, sequence))

users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234")
]

list = {i[1]: i for i in users}

username_mapping = {i[1]: i for i in users}
print(username_mapping)

for i in users:
    print("i[1]:i")


persons = [
    ("CNP", "USERNAME", "LASTNAME", "PASSWORD"),
    (25678854165848, "Bob", "UDFDGFN", "575755672567"),
    (11564845448465, "Rolf", "UFSGTEGT", "bob123@d"),
    (25234864514584, "Jose", "GTYROBRFGT", "!longp4assword"),

]

list = {i[2]: i for i in persons}
print(list)

extraction_1 = {i[0]: i for i in persons}
print(extraction_1)

extraction_2 = {i[1]: i for i in persons}
print(extraction_2)

extraction_3 = {i[1]: i for i in persons}
print(extraction_3["Bob"])
print(extraction_3["Rolf"])
print(extraction_3["Jose"])











