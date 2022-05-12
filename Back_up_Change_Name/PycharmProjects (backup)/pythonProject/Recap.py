from pathlib import Path


def happy_day(day):
    if day == "monday":
        return ":) It's monday !"
    if day != "monday":
        return ":D It's not the first day in the week. Maybe it's weekend !"


print(happy_day("sunday"))
print(happy_day("saturday"))
print(happy_day("monday"))

with open("myfile.txt", 'w') as myfiles:
    print("Hello!. What are you doing ?\t Happy Monday!", file=myfiles)

with open("One day Python.py", "w") as file:
    print("Inside, a lot of code,\nfor a day with Python", file=file)

with open("Excel_Python.xlsx", 'w') as myfile:
    print("First column\tSecond column\nFirst row\tSecond row", file=myfile)

with open("Python day and the challenges.odt", 'w') as myfile:
    print("Code \n", file=myfile)


# with open("Python day and the challenges.odt", 'w') as myfile:
#     import pathlib
#     if __name__ == '__main__':
#    file_location= pathlib.Path(__file__).parent.resolve()
#     print(parent_location, file = myfile)


with open("Python_Encapsulation.py", 'w') as myfile:
    print("Code \n", file=myfile)