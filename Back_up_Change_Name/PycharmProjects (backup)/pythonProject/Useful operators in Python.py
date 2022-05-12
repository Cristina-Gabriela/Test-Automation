# input functions:
index_count = 0

for i in "abcde":
    print("The index is {} and has the letter: {} ".format(index_count, i))
    index_count += 1

index = 0

for i in "Abracadabra":
    print("The key word is {} and the index is: {}".format(i, index))
    index += 1
print("Finish")

index_2 = 0
word = "Abracadabra"
for x in (word):
    print(word[index_2])
    index_2 += 1
print("Finish")

phrase = "IT course soon"
for x in enumerate(phrase):
    print(x)

IT_COURSE = "Automation Tester Python"
for index, letter in enumerate(IT_COURSE):
    print(index)
    print(letter)
for x in enumerate(IT_COURSE):
    print(x)

IT_course = ["Automation", "Tester", "Python"]
number = [3, 2, 1]
name = ["Cristina", "Cristina", "Cristina"]
print(zip(IT_course, number))
for correlation in zip(IT_course, number, name):
    print(correlation)

print(list(zip(IT_course, number, name)))
a = list(zip(IT_course, number, name))

print("Automation" in IT_course)
print("Manual" in IT_course)

print("Automation" in {"Automation": "Good"})
print("Manual" in {"Automation": "Good"})

print(min(number))
print(max(number))

from random import shuffle

number = [3, 2, 1, 20, 25, 56, 565]
shuffle(number)
print(number)

from random import randint

print(randint(0, 1000))

Automation = input("Enter a number: ")
print(type(Automation))
print(float(Automation))
print(int(Automation))
