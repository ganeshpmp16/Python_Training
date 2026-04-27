#function to add two numbers
from unittest import result

#defining the function
def add(a, b):
    return a + b
#taking user input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
#calling the add function   
result = add(num1, num2)
print("The sum of", num1, "and", num2, "is", result)