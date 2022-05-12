my_set = {1, 2, 3, 5, 56, 89, 21, 10, 102, 1359, 8741, 889885, 123, 1}
print(my_set)
print(type(my_set))
print(list(my_set))
list = [1, 2, 3, 5, 102, 8741, 10, 1359, 21, 56, 89, 123, 889885]
print(type(list))

new_list = [2, 5, 8, 8, 9, 5, 232, 565, 4547, 1, 8741, 1, 21, 102, 123, 8, 5, 2, 123, 102, 21]
print(set(new_list))
# new set= {1, 2, 4547, 5, 8741, 102, 8, 9, 232, 565, 21, 123} # without duplicate

# add 100 in my_set:
my_set.add(100)
print(my_set)

my_set1 = {1, 2, 3, 5, 56, 89, 21, 10, 102, 1359, 8741, 889885, 123, 1}
my_set2 = {1, 2, 4547, 5, 8741, 102, 8, 9, 232, 565, 21, 123}

print(my_set1.difference(my_set2)) # difference
print(my_set1.intersection(my_set2)) # intersection

x = my_set1.difference(my_set2)
print(x)
y = my_set1.intersection(my_set2)
print(y)
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())
print(my_set.pop())

=





