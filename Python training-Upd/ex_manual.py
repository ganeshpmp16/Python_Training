# raise exceptions in python manually
def calculate_square_root(number):
    if number < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return number ** 0.5
try:
    num = -4
    result = calculate_square_root(num)
    print(f"The square root of {num} is: {result}")
except ValueError as e:
    print("Error:", e)