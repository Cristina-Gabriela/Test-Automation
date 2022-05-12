str = "Ursul pacalit de vulpe, vulpite, vulpoi"
count = 0

for x in str:
    if (x == "v"):
        count += 1
print(count)


dictionar = list(range(10))
print(dictionar)

dictionar = list(range(0,10))
print(len(dictionar))

abc = list(range(50))
print(len(abc))
print(abc)

nums = list(range(3, 15, 3))
print(nums)
print(nums[2])


for i in range (0,20,2):
    print(i)

list = [1,1,2,3,5,8,13]
print(list[list[4]])

for i in range(10):
    if not i %2 == 0:
        print(i+1)

for i in range(5):
    if i%2 == 0:
        print(i+1)

for i in range(10):
    if not i%2 == 0:
        print(i+1)

for i in range(10):
    if i%2 == 0:
        print(i+1)

while False:
    print("Looping")

list = [1,2,3,4]
if len(list)%2 == 0:
    print(list[0])

list =[1,2,3,4]
if len(list) %2 ==0:
    print(list[0])

def TGV (word):
    print("vreau sa dezvolt caile ferate introducand o retea de trenuri tgv: " + word)
TGV("cu o viteza de 600 km/h")
TGV("pe intreaga suprafata a Romaniei")
TGV("de la Vest la Est si de la Nord la Sud")

def pret(x, y, z, a):
    print(x+y)
    print(x-y)
    print(x**y-y**a)
    print(z-y+a**x)

pret(2,3,4,5)

def even(x):
    if x%2 == 0:
        print("OK")
    else:
        print("no")




def max(x, y):
    if x>= y:
        return x
    else:
        return y
print(max(5,6))

def max(x, y):
    if x >= y:
        return x
    else:
        return y
print(max(2,5))
x(min(5,3))
print(max(56, 56))
print(max(56, 89))
































