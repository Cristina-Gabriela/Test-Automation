import random
secret_number = random.randint(0, 5)
guess_number = -1
while secret_number != guess_number:
    guess_number = int(input("Please enter a number between 0 and 5: "))
    if secret_number == guess_number:
        print("You are a genius !")
    else:
        print("Keep trying")

import random
user_number = random.randint(0, 5)
guess_number = -1
while user_number != guess_number:
    guess_number = int(input("Please enter a number between 0 and 5: "))
    if user_number == guess_number:
        print("You are a genius!")
    else:
        print("Not ok")
print("Finish")

import random
list = random.randint(0, 7)
lucky_number = -1

while lucky_number != list:
    lucky_number = int(input("Enter a number and see if he's lucky"))
    if lucky_number == list:
        print("This is your lucky number")
    else:
        print("Your lucky number is smaller")


mario = 3
while mario > 0:
    print("Mario has lives")
    mario = mario - 1
if mario == 1:
    print("Mario, beware, you only have one more life!")
print("You lost your life")


pokemon = 17
while pokemon > 0:
    print("You have moved on to the next level")
    pokemon = pokemon - 1
if pokemon == 1:
    print("You won the last round of pokemon")
print("You are a winner!")

a = 12
while a > 0:
    print("Watch your favorite cartoon series: Tom & Jerry")
    a = a - 1
if a == 1:
    print("You've finished watching the Tom & Jerry cartoon series.")
print("Congratulation!")

