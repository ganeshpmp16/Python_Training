def calcuate(a,b=10):
    return a+b, a-b, a*b, a/b
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
addition, subtraction, multiplication, division = calcuate(num1, num2)
print("Addition:", addition)
print("Subtraction:", subtraction)  
print("Multiplication:", multiplication)
print("Division:", division)
