# Functions:
def my_function(*student):
    print("The youngest student is" + student[0])


my_function("Cristina", "Python", "Linux")


# refactor the function to print out all the students

def my_function(**student):
    print("The student name is " + student["name"])
    print("It's salary is " + student["salary"])
    print("And email" + student["mail"])
# update the code to display the salary and email

my_function(name="Cristina", salary="0k euro", mail="python@snake.com")


def pret(*pret_produs):
    print("Miere_de_albini: " + pret_produs[0])
    print("Mere:" + pret_produs[1])
    print("Struguri: " + pret_produs[2])


pret("100", "50", "80")



def tehnologie(caracteristica_2=None, caracteristica_1=None, **model, **display):
    print("Laptop Dell" + model[caracteristica_1] + display[dimensiune_1])
    print("Laptop Accer" + model[caracteristica_2] + display[dimensiune_2])
    print("Laptop Hp" + model[caracteristica_3] + display[dimensiune_3])


tehnologie(caracteristica_1="Intel_core_i7","15, 6_Full_HD_Dispay", dimensiune_1="15, 6_Full_HD_Dispay", caracteristica_2="Intel_Core_i5",dimensiune_1="13, 3_HD_Display", caracteristica_3="Intel_core_i3", 10, dimensiune_3="1_Display")



def tehnologie(**model):
    print("Laptop Dell" + model["caracteristica_1"])
    print("Laptop Accer" + model["caracteristica_2"])
    print("Laptop Hp" + model["caracteristica_3"])


tehnologie(caracteristica_1="Intel_core_i7:\n15, 6_Full_HD_Dispay", caracteristica_2="Intel_Core_i5:\n13, 3_HD_Display",
           caracteristica_3="Intel_core_i3:\n1_Display")


def melodie(*versuri):
    print("Aceasta este o melodie despre: " + versuri[0])
    print("Aceasta este o melodie despre: " + versuri[1])
    print("Aceasta este o melodie despre: " + versuri[2])
    print("Aceasta este o melodie despre: " + versuri[3])
    print("Aceasta este o melodie despre: " + versuri[4])


melodie("casa mea", "mesageri indepartati", "sa vii in gand", "al meu gand", "acorduri ample")


def planeta(*bucurie):
    print("Pe planeta este " + bucurie[0])
    print("Pe planeta ar putea fi " + bucurie[1])
    print("Pe aceasta planeta este " + bucurie[2])
    print("Pe alta planeta " + bucurie[3])


planeta("multa bucurie pentru unii", "bucurie si pentru mine", "loc pentru toti", "trebuie sa ajunga multa bucurie")


def planeta(**bucurie):
    print("Pe planeta este " + bucurie["descriere_0"])
    print("Pe planeta ar putea fi " + bucurie["descriere_1"])
    print("Pe aceasta planeta este " + bucurie["descriere_2"])
    print("Pe alta planeta " + bucurie["descriere_3"])


planeta(descriere_0="multa bucurie pentru unii", descriere_1="bucurie si pentru mine", descriere_2="loc pentru toti",
        descriere_3=
        "trebuie sa ajunga multa bucurie")






# picture = [
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 1, 1, 0, 0],
#     [0, 1, 1, 1, 1, 1, 0],
#     [1, 1, 1, 1, 1, 1, 1],
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 0, 1, 0, 0, 0]
# ]
# # 1.Refactor the triangle and rectangle problems using functions
# # 2.Calculate the sum of all the elements from a list using an iterable
