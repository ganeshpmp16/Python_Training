import math_utlils
# using the math utilities
a = 10
b = 5
print("Addition:", math_utlils.add(a, b))  # prints 15
print("Subtraction:", math_utlils.subtract(a, b))  # prints 5
print("Multiplication:", math_utlils.multiply(a, b))  # prints 50
print("Division:", math_utlils.divide(a, b))  # prints 2.0
print("Division by zero test:")
try:
    math_utlils.divide(a, 0)
except ValueError as e:
    print(e)  # prints "Denominator cannot be zero."
    
