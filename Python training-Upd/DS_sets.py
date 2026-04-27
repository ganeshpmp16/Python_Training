# to demonstrate the use of a set as a data structure
# a set is a collection of items that are unordered and unindexed
# sets are written with curly braces
my_set = {"apple", "banana", "cherry"}
print(my_set)
# to check if an item is in a set, you can use the in keyword
print("apple" in my_set)  # prints True
print("banana" in my_set)  # prints True
print("date" in my_set)  # prints False
# you can add items to a set using the add() method
my_set.add("date")
print(my_set)  # prints {"apple", "banana", "cherry", "date"}
# you can also add multiple items to a set using the update() method
my_set.update(["elderberry", "fig", "grape"])
print(my_set)  # prints {"apple", "banana", "cherry", "date", "elderberry", "fig", "grape"}
# you can remove items from a set using the remove() method, which raises an error if the item is not found
my_set.remove("banana")
print(my_set)  # prints {"apple", "cherry", "date", "elderberry", "fig", "grape"}
# you can also remove items from a set using the discard() method, 
#   which does not raise an error if the item is not found
my_set.discard("banana")  # does not raise an error
print(my_set)  # prints {"apple", "cherry", "date", "elderberry", "fig", "grape"}
# you can get the length of a set using the len() function
print(len(my_set))  # prints 6
# you can loop through a set using a for loop
for item in my_set:
    print(item)
# prints the items in the set on separate lines (order may vary)
# sets do not allow duplicate items 
my_set.add("apple")
print(my_set)  # prints {"apple", "cherry", "date", "elderberry", "fig", "grape"}
# you can also create a set of numbers
numbers = {1, 2, 3, 4, 5}
print(numbers)  # prints {1, 2, 3, 4, 5}
# you can perform operations on sets, such as union, intersection, and difference
set1 = {1, 2, 3}
set2 = {3, 4, 5}
# union
union_set = set1.union(set2)
print(union_set)  # prints {1, 2, 3, 4, 5}
# intersection
intersection_set = set1.intersection(set2)
print(intersection_set)  # prints {3}
# difference
difference_set = set1.difference(set2)
print(difference_set)  # prints {1, 2}
# symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # prints {1, 2, 4, 5}  
