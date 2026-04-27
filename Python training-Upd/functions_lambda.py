# lambda functions are anonymous functions defined using the lambda keyword. They can take any number of arguments but can only have one expression. The syntax is: lambda arguments: expression
# Example of a lambda function to add two numbers
add = lambda x, y: x + y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2)
print("The sum of", num1, "and", num2, "is", result)    
# Example of a lambda function to find the square of a number
square = lambda x: x ** 2
num = int(input("Enter a number to find its square: "))
result = square(num)
print("The square of", num, "is", result)
# Example of a lambda function to find the maximum of two numbers
maximum = lambda x, y: x if x > y else y
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = maximum(num1, num2)
print("The maximum of", num1, "and", num2, "is", result)
