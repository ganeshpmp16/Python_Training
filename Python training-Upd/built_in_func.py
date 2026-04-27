# import a specific built-in function
from math import sqrt
# using the imported sqrt function
number = 16
result = sqrt(number)
print(f"The square root of {number} is {result}.")  # prints "The square root of 16 is 4.0."    
# import with alias
import math as m
# using the math module with alias
print("Square root of 25:", m.sqrt(25))  # prints 5.0
print("Sine of 30 degrees:", m.sin(m.radians(30)))  # prints 0.5
print("Cosine of 60 degrees:", m.cos(m.radians(60)))  # prints 0.5
print("Pi:", m.pi)  # prints 3.141592653589793

# import multiple functions from a module
from math import sqrt, sin, cos, radians
# using the imported functions
print("Square root of 36:", sqrt(36))  # prints 6.0
print("Sine of 45 degrees:", sin(radians(45)))  # prints 0.7071067811865475
print("Cosine of 60 degrees:", cos(radians(60)))  # prints  0.5

