# to demonstrate the use of a list as a data structure
# a list is a collection of items that are ordered and changeable
# lists are written with square brackets
my_list = ["apple", "banana", "cherry"]
print(my_list)
# to access an item in a list, you can use its index
print(my_list[0])  # prints "apple"
print(my_list[1])  # prints "banana"
print(my_list[2])  # prints "cherry"
# you can also use negative indexing to access items from the end of the list
print(my_list[-1])  # prints "cherry"
print(my_list[-2])  # prints "banana"
print(my_list[-3])  # prints "apple"
# you can change the value of an item in a list by accessing its index and assigning a new value
my_list[1] = "blueberry"
print(my_list)  # prints ["apple", "blueberry", "cherry"]
# you can add items to a list using the append() method
my_list.append("date")
print(my_list)  # prints ["apple", "blueberry", "cherry", "date"]
# you can also add items to a list using the insert() method, which allows you to specify the index where the new item should be added
my_list.insert(1, "banana")
print(my_list)  # prints ["apple", "banana", "blueberry", "cherry", "date"]
# you can remove items from a list using the remove() method, which removes the first occurrence of the specified value
my_list.remove("banana")
print(my_list)  # prints ["apple", "blueberry", "cherry", "date"]
# you can also remove items from a list using the pop() method, which removes the item at the specified index and returns it
removed_item = my_list.pop(1)
print(removed_item)  # prints "blueberry"
print(my_list)  # prints ["apple", "cherry", "date"]    
# you can get the length of a list using the len() function
print(len(my_list))  # prints 3
# you can check if an item is in a list using the in keyword
print("apple" in my_list)  # prints True
print("banana" in my_list)  # prints False
# you can loop through a list using a for loop
for item in my_list:
    print(item)
# prints "apple", "cherry", "date" on separate lines 
# allow duplicates in a list
my_list.append("apple")
print(my_list)  # prints ["apple", "cherry", "date", "apple"]
# you can also create a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)  # prints [1, 2, 3, 4, 5]
# you can perform operations on lists, such as concatenation and repetition
# concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated_list = list1 + list2      
print(concatenated_list)  # prints [1, 2, 3, 4, 5, 6]
# repetition
repeated_list = list1 * 3
print(repeated_list)  # prints [1, 2, 3, 1, 2, 3, 1, 2, 3]
#find the maximum and minimum values in a list of numbers
max_value = max(numbers)
min_value = min(numbers)
print("Max value:", max_value)  # prints "Max value: 5" 
print("Min value:", min_value)  # prints "Min value: 1" 
# sort a list of numbers in ascending order
numbers.sort()
print("Sorted list:", numbers)  # prints "Sorted list: [1, 2, 3, 4, 5]"
# sort a list of numbers in descending order
numbers.sort(reverse=True)
# to reverse the order of a list, you can use the reverse() method
numbers.reverse()
print("Reversed list:", numbers)  # prints "Reversed list: [5, 4, 3, 2, 1]" 
