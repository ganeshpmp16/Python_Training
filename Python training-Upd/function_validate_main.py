# validation demo using functions
def add(x, y):
    return x + y
def get_number(prompt): # function to get a valid integer input from the user
    while True:
        try:
            return int(input(prompt)) # this will attempt to convert the input to an integer
        except ValueError: # if the conversion fails, it will raise a ValueError, which we catch and prompt the user again
            print("Invalid input. Please enter a valid integer.")

def main(): # main function is the entry point of the program like c# and java where the execution starts from main function
    num1 = get_number("Enter first number: ")
    num2 = get_number("Enter second number: ")
    result = add(num1, num2)
    print("The sum of", num1, "and", num2, "is", result)

if __name__ == "__main__":
    main()