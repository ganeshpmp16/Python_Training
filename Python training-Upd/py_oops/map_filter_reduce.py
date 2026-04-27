# functional programming tools are map, filter, and reduce
# map applies a function to all the items in an iterable and returns a new iterable with the results
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]
# filter creates a new iterable with all the items that satisfy a condition
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4] 
# reduce applies a function of two arguments cumulatively to the items of an iterable, from left to right, to reduce the iterable to a single value
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120
#filter and map together
squared_even_numbers = map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers))
print(list(squared_even_numbers))  # Output: [4, 16]
