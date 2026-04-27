# to demonstrate the use of a tuple as a data structure
# a tuple is a collection of items that are ordered and unchangeable
# tuples are written with parentheses
my_tuple = ("apple", "banana", "cherry")
print(my_tuple)
# to access an item in a tuple, you can use its index
print(my_tuple[0])  # prints "apple"
print(my_tuple[1])  # prints "banana"
print(my_tuple[2])  # prints "cherry"
# you can also use negative indexing to access items from the end of the tuple
print(my_tuple[-1])  # prints "cherry"
print(my_tuple[-2])  # prints "banana"
print(my_tuple[-3])  # prints "apple"
# you cannot change the value of an item in a tuple (tuples are immutable)
# you can add items to a tuple by creating a new tuple with the additional items
my_tuple = my_tuple + ("date",)
print(my_tuple)  # prints ("apple", "banana", "cherry", "date")
# you can get the length of a tuple using the len() function
print(len(my_tuple))  # prints 4
# you can check if an item is in a tuple using the in keyword
print("apple" in my_tuple)  # prints True
print("banana" in my_tuple)  # prints True
# you can loop through a tuple using a for loop
for item in my_tuple:
    print(item)
# prints "apple", "banana", "cherry", "date" on separate lines 
# you can also create a tuple of numbers
numbers = (1, 2, 3, 4, 5) 
print(numbers)  # prints (1, 2, 3, 4, 5)
# you can perform operations on tuples, such as concatenation and repetition
# concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # prints (1, 2, 3,4, 5, 6)
# repetition
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # prints (1, 2, 3, 1, 2, 3, 1, 2, 3)
# find the maximum and minimum values in a tuple of numbers
max_value = max(numbers)
min_value = min(numbers)
print("Max value:", max_value)  # prints "Max value: 5"
print("Min value:", min_value)  # prints "Min value: 1"
# tuple with one item
single_item_tuple = ("apple",)
print(single_item_tuple)  # prints ("apple",)
print(type(single_item_tuple))  # prints <class 'tuple'>
# if you don't include the comma, it will be treated as a string    
not_a_tuple = ("apple")
print(not_a_tuple)  # prints "apple"    
print(type(not_a_tuple))  # prints <class 'str'>
# you can also create a tuple without parentheses, using just commas
tuple_without_parentheses = "apple", "banana", "cherry"
print(tuple_without_parentheses)  # prints ("apple", "banana", "cherry")
print(type(tuple_without_parentheses))  # prints <class 'tuple'>
# you can unpack a tuple into separate variables
fruit1, fruit2, fruit3,fruit4 = my_tuple
print(fruit1)  # prints "apple"
print(fruit2)  # prints "banana"
print(fruit3)  # prints "cherry"
print(fruit4)  # prints "date"
# you can also use the * operator to unpack a tuple into a list
fruits = *my_tuple,
print(fruits)  # prints ["apple", "banana", "cherry", "date"]
print(type(fruits))  # prints <class 'list'>
# operations on tuples
# you can use the count() method to count the number of occurrences of a specific value in a tuple
my_tuple = ("apple", "banana", "cherry", "apple")
count_apple = my_tuple.count("apple")
print(count_apple)  # prints 2  
# you can use the index() method to find the index of the first occurrence of a specific value in a tuple
index_banana = my_tuple.index("banana")
print(index_banana)  # prints 1
# since tuples are immutable, they do not have methods for adding, removing, or changing items like lists do.#
#looping through a tuple using a for loop
for item in my_tuple:
    print(item)
# prints "apple", "banana", "cherry", "apple" on separate lines 
# loops through a tuple using a while loop
i = 0
while i < len(my_tuple):
    print(my_tuple[i])
    i += 1
# prints "apple", "banana", "cherry", "apple" on separate lines
# loop with index and value using enumerate()
for index, item in enumerate(my_tuple):
    print(f"Index: {index}, Item: {item}")
# prints "Index: 0, Item: apple", "Index: 1, Item: banana", "Index: 2, Item: cherry", "Index: 3, Item: apple" on separate lines 
# looping through tuple of tuples
tuple_of_tuples = (("apple", "red"), ("banana", "yellow"), ("cherry", "red"))
for fruit, color in tuple_of_tuples:
    print(f"The {fruit} is {color}.") # print with f-string to format the output    
# prints "The apple is red.", "The banana is yellow.", "The cherry is red." on separate lines     
# you can also use a for loop with unpacking to loop through a tuple of tuples
for item in tuple_of_tuples:
    fruit, color = item
    print(f"The {fruit} is {color}.") # print with f-string to format the output
# prints "The apple is red.", "The banana is yellow.", "The cherry is red." on separate lines   
# you can also use a while loop with unpacking to loop through a tuple of tuples
i = 0
while i < len(tuple_of_tuples):
    fruit, color = tuple_of_tuples[i]
    print(f"The {fruit} is {color}.") # print with f-string to format the output
    i += 1
# prints "The apple is red.", "The banana is yellow.", "The cherry is red." on separate lines   
# Loop nested tuples
nested_tuple = (("apple", ("red", "green")), ("banana", ("yellow", "green")), ("cherry", ("red", "dark red")))
for fruit, colors in nested_tuple:
    color1, color2 = colors
    print(f"The {fruit} can be {color1} or {color2}.") # print with f-string to format the output  
