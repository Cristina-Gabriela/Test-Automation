male_rabbits = int(input("Number of male rabbits"))
female_rabbits = int(input("Number of female rabbits"))

if male_rabbits > 0 and female_rabbits > 0:
    breed = input("Do you want to breed ?").lower()
    if breed == "yes":
        print("ok")
    else:
        print("keep them apart!")
# To do: convertire intr-o functie
# nr de rabbits + nr. de breed


breed = male_rabbits + female_rabbits
print(breed)

def breed(male_rabbits,female_rabbits):
    male_rabbits = int(input('Enter a number : '))
    female_rabbits = int(input('Enter a number: '))
print(f"The number of male rabbits is : {male_rabbits} and the number of female rabits is:{female_rabbits} ")

