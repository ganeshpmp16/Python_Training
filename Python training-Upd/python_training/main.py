#main.py is the entry point of the program
from mypackage.calc import add, subtract
from mypackage.greet import greet
def main():
    # Greet the user
    name = "Alice"
    greeting = greet(name)
    print(greeting)
    
    # Perform some calculations
    x = 10
    y = 5
    sum_result = add(x, y)
    diff_result = subtract(x, y)
    
    print(f"The sum of {x} and {y} is: {sum_result}")
    print(f"The difference between {x} and {y} is: {diff_result}")

if __name__ == "__main__":
    main()
    