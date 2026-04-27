# import math modul;e for mathematical functions like pow,factorial,log etc
import math
# using the math module
print("Square root of 16:", math.sqrt(16))  # prints 4.0
#pow function
print("2 raised to the power of 3:", math.pow(2, 3))  # prints 8.0
#factorial function
print("Factorial of 5:", math.factorial(5))  # prints 120
#log function
print("Logarithm of 100 to base 10:", math.log10(100))  # prints 2.0
print("Logarithm of 8 to base 2:", math.log2(8))  # prints 3.0
# importing the random module for generating random numbers
import random
# using the random module
print("Random integer between 1 and 10:", random.randint(1, 10))  # prints a random integer between 1 and 10
print("Random float between 0 and 1:", random.random())  # prints a random float between 0 and 1
# choice function to select a random element from a list
my_list = ["apple", "banana", "cherry"]
print("Random choice from the list:", random.choice(my_list))  # prints a random element from the list  
# shuffle function to shuffle a list
random.shuffle(my_list)
print("Shuffled list:", my_list)  # prints the list in a random order   
# date and time module for working with dates and times
import datetime
# using the datetime module
current_date = datetime.date.today()
print("Current date:", current_date)  # prints the current date in the format YYYY-MM-DD
current_time = datetime.datetime.now().time()
print("Current time:", current_time)  # prints the current time in the format HH:MM:SS.microseconds
current_datetime = datetime.datetime.now()
print("Current date and time:", current_datetime)  # prints the current date and time in the format YYYY-MM-DD HH:MM:SS.microseconds    
# import the os module for interacting with the operating system

