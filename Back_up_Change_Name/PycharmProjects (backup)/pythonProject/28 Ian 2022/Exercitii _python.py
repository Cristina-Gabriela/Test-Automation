# if else:
male_rabbits = int(input("Number of male rabbits: "))
female_rabbits = int(input("Number of female rabbits: "))

if male_rabbits > 0 and female_rabbits > 0:
    breed = input("Do you want to breed ?").lower()
    if breed == "yes":
        print("ok")
    else:
        print("Keep them apart !")

# To do: convertire intr-o functie
# nr de rabbits + nr. de breed
# loop control:

# TO DO : Sa introducem un interval de numere (1,10) de la consola, sa generezam random o valoare din acel interval,
# dupa care sa-i cerem userului sa introduca un nr. de la 1 la 10, sa-l ghiceasca
# daca am gasit raspunsul corect, printam "You are a genius", daca nu, "keep trying".
# def my_sum()
