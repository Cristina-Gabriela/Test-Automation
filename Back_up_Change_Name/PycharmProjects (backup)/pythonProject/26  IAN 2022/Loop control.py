my_list = [10, 23, 56, 78, 12, 12, 56, 100, 123, 456]
print(sum(my_list))

s = 0
for i in my_list:
    s += i
print(s)

s = 0
for i in my_list:
    s += i
    print(s)  # diferit de a doua 10, 33,.....926 (sum)

s = 0
for i in my_list:
    s += i
else:  # sa nu depasesti suma. Din motive de logare.
    print("Sum already calculated !")
print(s)

# suma dupa index:
s = 0
for a in range(0, len(my_list)):
    s += my_list[a]
print(s)

# suma prin while
x = 0
while x < len(my_list):
    s += my_list[x]
    x += 1
print(s)

# TO DO : Sa introducem un interval de numere (1,10) de la consola, sa generezam random o valoare din acel interval,
# dupa care sa-i cerem userului sa introduca un nr. de la 1 la 10, sa-l ghiceasca
#daca am gasit raspunsul corect, printam "You are a genius", daca nu, "keep trying".
# def my_sum()
