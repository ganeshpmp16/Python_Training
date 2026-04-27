def add_numbers(x, y):
    return x + y

def main():
    count = int(input("How many pairs of numbers do you want to add? "))
    numbers = []
    for i in range(count):
        num1 = int(input(f"Enter first number for pair {i + 1}: "))
        num2 = int(input(f"Enter second number for pair {i + 1}: "))
        numbers.append((num1, num2))

    for num1, num2 in numbers:
        result = add_numbers(num1, num2)
        print("The sum of", num1, "and", num2, "is", result)

if __name__ == "__main__":
    main()