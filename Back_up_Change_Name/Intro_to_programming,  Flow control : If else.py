s = 100
f = 56
if s < f:
    print("S is not bigger than f")
elif s == f:
    print("S is equal with f")
elif s > f:
    print("S is bigger than f")
else:
    print("No correlation between s and f")

i = 20
b = 25
f = 50
if i == b > f:
    print("False")
elif i < b < f:
    print("True")
print("Finish")

a = 20
if a > 5:
    print("Bigger than 5")
if a > 10:
    print("Bigger than 10")
    if a >= 20:
        print("Bigger or equal with 20")
        pass
        #        if a > 100:
        #            print("A is bigger than 100")
        #            pass
        if a > 2:
            print("It's ok")
            pass
            if a > 21:
                print("Is biggest ?")
                pass
                if a > 14:
                    print("Is ok again")

print("Finish")

today = int(input("Enter the day: > 31"))
if today >= 0:
    if today == 2:
        print('Today is 2 february')
    else:
        print("Another day")

city = "Monaco"

if city == "New York":
    print("New York")
elif city == "Dubai":
    print("Dubai")
elif city == "Dorohoi":
    print("Dorohoi")
else:
    print("No city found: Error 404")




















