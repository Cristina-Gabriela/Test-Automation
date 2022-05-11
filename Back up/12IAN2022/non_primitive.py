a = [1, 2, 5, 7]
b = ["hello", "hi", "bonjour"]
c = [45, "ca va, bien?", True, 3.5, "bien", [1.2, [True, False]]]
e = [45, "ca va?", True, 3.5, "bien", c]
d = len(c)

print(c[0])
print(c[-1])
print(len(a))
print(c[d - 1])
print(e)
print(e[-1])
print(e[-1][1])
print(e[-1][-1][-1][-1])

a = [10, 20, 30, 25, 56]
b = ["investments", "tehnology", "2021", "winnings"]
c = [10, [True, False], 3.5, 10, 56, 36, 5656, True, False, "tehnology", "investments"]
e = [20, 65, "investments", "tehnology", 5.2, [True, False], c]
d = len(a) + len(b)
f = len(a) ** len(e)

print(a[2])
print(b[0])
print(b[-1])
print(len(a))
print(e)
print(e[-1])
print(e[-1][-1])
print(e[-2][-1])