<<<<<<< HEAD
import my_own
import random
print(my_own.PI)
#generates random numbers between one and ten
random_numbers=random.randint(1,10)
print(random_numbers)
#genretes random numbers between 0 and 0.999999 not including 1ss
print(random.random())



#understanding python lists 
names= ["kingsley", "brandon", "faith"]
print(names)
#adding items to a list: append() method
names.append("victory")
print(names)
#how to access items in python
print(f"kignsley: {names[0]}")
#how many items are in list
lenth=len(names)
print(lenth)
#inserting an item into a list at specific index
names.insert(2,"desmond")
print(names)
#POPPING REMOVING FROM LIST
item_removed=names.pop(1)
print("after removing items from index 1")
print(names)
#REMOVE METHOD
no_sorry=names.remove("faith")
print(names)
#SLICING
# A LIST OF NUMBERS
my_numbers=[12,24,36,48,63]
# [x:y]-. getting elements between x and y, including x but not including y
print("SLICING___")
print(my_numbers[1:3])
#[:x] printing from first item to but not including x
print(my_numbers[:3])
#reverse items in a list
#[::-1]
=======
import my_own
import random
print(my_own.PI)
#generates random numbers between one and ten
random_numbers=random.randint(1,10)
print(random_numbers)
#genretes random numbers between 0 and 0.999999 not including 1ss
print(random.random())



#understanding python lists 
names= ["kingsley", "brandon", "faith"]
print(names)
#adding items to a list: append() method
names.append("victory")
print(names)
#how to access items in python
print(f"kignsley: {names[0]}")
#how many items are in list
lenth=len(names)
print(lenth)
#inserting an item into a list at specific index
names.insert(2,"desmond")
print(names)
#POPPING REMOVING FROM LIST
item_removed=names.pop(1)
print("after removing items from index 1")
print(names)
#REMOVE METHOD
no_sorry=names.remove("faith")
print(names)
#SLICING
# A LIST OF NUMBERS
my_numbers=[12,24,36,48,63]
# [x:y]-. getting elements between x and y, including x but not including y
print("SLICING___")
print(my_numbers[1:3])
#[:x] printing from first item to but not including x
print(my_numbers[:3])
#reverse items in a list
#[::-1]
>>>>>>> refs/remotes/origin/main
print(my_numbers[::-1])