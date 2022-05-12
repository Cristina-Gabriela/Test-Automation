y = {f: f * f for f in range(50) if f % 5 == 1}
print(y)

y = {}.fromkeys(["mouse", "laptop", "desk"], 50)
print(y)
print(len(y))
print(y.popitem())
print(y)
y.clear()
print(y)
y = {}.fromkeys(["mouse", "laptop", "desk"], 50)
print(y["mouse"])
print(y["laptop"])
print(y["desk"])
print(y.get("mouse"))
y["mouse"] = 51
y["laptop"] = 102
y["desk"] = 56
print(y)
y["mobile"] = 25
print(y)
d = {}.fromkeys(["news", "youtube", "google", "gmail"], 25)
print(d)

print(d["news"])
print(d["youtube"])
print(d["google"])
print(d["gmail"])
d["py"] = 26
print(d)
d["news"] = 28
print(d)
d["youtube"] = 30
print(d)
print(len(d))
print(d.popitem())
print(d)
for x in d.items():
    print(x)

a = {x: x ** x for x in range(50) if x % 2 == 1}
print(a)
d = {v: v ** v for v in range(50) if v % 10 == 1}
print(d)

# inverse keys & values
my_maps = {1: "54", 9: "12", 13: "78", 21: "7", 12: "48", 45: "78"}
print(sorted(my_maps))
inv_map = {v: k for k, v in my_maps.items()}
print(inv_map)
inv_map = {'54': 1, '12': 9, '78': 45, '7': 21, '48': 12}
print(inv_map.keys())
print(inv_map.values())
print(inv_map["54"])
inv_map["54"] = 10
print(inv_map)
new_map = {k: v for v, k in inv_map.items()}
print(new_map)

# add a key to a dictionary
a = {0: 10, 1: 20, 2: 50, 3: 56, 4: 56}
a["2"] = 30
print(a)
a["20"] = 100
print(a)
a["56"] = 23
print(a)

# Concatenate 3 dictionaries:
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}


def Merge(dict1, dict2):
    return (dict2.update(dict1))


print(Merge(dict1, dict2))
print(dict2)


def Merge(dict2, dict3):
    return (dict3.update(dict2))


print(Merge(dict2, dict3))
print(dict3)

# To check if a given key already exist:
dict1 = {1: "10", 2: "20"}
dict2 = {3: "30", 4: "40"}
print(any(dict1))
print(any(dict1[1]))
print(any(dict2[3]))

# to generate and print a dictionary that contains a Number (between 1 and n) in the form (x, x*x)
# n= 5
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# my_dict ={x:x*x, for x in my_dict,if% 1 ==5}
#    print(my_dict)


n = int(input("Input a number: "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x
print(d)

n = int(input("Input a number :  "))
d = dict()

for x in range(1, n + 1):
    d[x] = x * x
print(d)
+ https://www.w3resource.com/python-exercises/dictionary/
+https://pynative.com/python-dictionary-exercise-with-solutions/














"""  
1. Write a Python script to sort (ascending and descending) a dictionary by value. Go to the editor

Click me to see the sample solution

2. Write a Python script to add a key to a dictionary. Go to the editor

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

Click me to see the sample solution

3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Click me to see the sample solution

4. Write a Python script to check whether a given key already exists in a dictionary. Go to the editor

Click me to see the sample solution

5. Write a Python program to iterate over dictionaries using for loops. Go to the editor

Click me to see the sample solution

6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Click me to see the sample solution

7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Go to the editor
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
Click me to see the sample solution

8. Write a Python script to merge two Python dictionaries. Go to the editor
Click me to see the sample solution

9. Write a Python program to iterate over dictionaries using for loops. Go to the editor
Click me to see the sample solution

10. Write a Python program to sum all the items in a dictionary. Go to the editor
Click me to see the sample solution

11. Write a Python program to multiply all the items in a dictionary. Go to the editor
Click me to see the sample solution

12. Write a Python program to remove a key from a dictionary. Go to the editor
Click me to see the sample solution

13. Write a Python program to map two lists into a dictionary. Go to the editor
Click me to see the sample solution

14. Write a Python program to sort a given dictionary by key. Go to the editor
Click me to see the sample solution

15. Write a Python program to get the maximum and minimum value in a dictionary. Go to the editor
Click me to see the sample solution

16. Write a Python program to get a dictionary from an object's fields. Go to the editor
Click me to see the sample solution

17. Write a Python program to remove duplicates from Dictionary. Go to the editor
Click me to see the sample solution

18. Write a Python program to check a dictionary is empty or not. Go to the editor
Click me to see the sample solution

19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
Click me to see the sample solution

20. Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
Click me to see the sample solution

1. Write a Python script to sort (ascending and descending) a dictionary by value. Go to the editor

Click me to see the sample solution

2. Write a Python script to add a key to a dictionary. Go to the editor

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}

Click me to see the sample solution

3. Write a Python script to concatenate following dictionaries to create a new one. Go to the editor

Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

Click me to see the sample solution

4. Write a Python script to check whether a given key already exists in a dictionary. Go to the editor

Click me to see the sample solution

5. Write a Python program to iterate over dictionaries using for loops. Go to the editor

Click me to see the sample solution

6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Click me to see the sample solution

7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys. Go to the editor
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}
Click me to see the sample solution

8. Write a Python script to merge two Python dictionaries. Go to the editor
Click me to see the sample solution

9. Write a Python program to iterate over dictionaries using for loops. Go to the editor
Click me to see the sample solution

10. Write a Python program to sum all the items in a dictionary. Go to the editor
Click me to see the sample solution

11. Write a Python program to multiply all the items in a dictionary. Go to the editor
Click me to see the sample solution

12. Write a Python program to remove a key from a dictionary. Go to the editor
Click me to see the sample solution

13. Write a Python program to map two lists into a dictionary. Go to the editor
Click me to see the sample solution

14. Write a Python program to sort a given dictionary by key. Go to the editor
Click me to see the sample solution

15. Write a Python program to get the maximum and minimum value in a dictionary. Go to the editor
Click me to see the sample solution

16. Write a Python program to get a dictionary from an object's fields. Go to the editor
Click me to see the sample solution

17. Write a Python program to remove duplicates from Dictionary. Go to the editor
Click me to see the sample solution

18. Write a Python program to check a dictionary is empty or not. Go to the editor
Click me to see the sample solution

19. Write a Python program to combine two dictionary adding values for common keys. Go to the editor
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
Click me to see the sample solution

20. Write a Python program to print all unique values in a dictionary. Go to the editor
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
Click me to see the sample solution

"""
