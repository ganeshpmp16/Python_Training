def add(x, y):
    return x + y
def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add(num1, num2)
    print("The sum of", num1, "and", num2, "is", result)

if __name__ == "__main__":
    main()