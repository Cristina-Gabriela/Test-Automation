
a: int = int(input("Salariu bun: "))
b: int = int(input("Motivatie crescuta:"))

if a > 0 and b > 0:
    FB = input("Salariul bun te motiveaza ? ").lower()
    if FB == "da":
        print("Salariul bun motiveaza")
    else:
        print("Motivatia nu este atat de mare cand salariul nu este bun")

my_list = [23, 45, 56, 78]
s = 0
for i in my_list:
    s += 1
print(s)

x = 0
print("Incepe de la 0")
for i in [23, 45, 56, 78]:
    x += i
    print(x, i)

viata_buna = 0
print("Incepe de la 0")
for i in [123, 1523, 15, 56, 3123, 5864, 2118, 2315]:
    viata_buna = viata_buna + 1
    print(viata_buna, i)
    viata_buna += i
    print(viata_buna)

it = 0
print("Incepem de la zero")
for x in [1, 2, 3]:
    it = it + x
    print(it)
it = 0
print("Incepem de la zero")
for x in [1, 2, 3]:
    it = it + 1
    print(it)




# listare
# suma
