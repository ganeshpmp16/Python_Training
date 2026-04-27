# custom exception in python
class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass
def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate the square root of a negative number.")
    return number ** 0.5
try:
    num = -4
    result = calculate_square_root(num)
    print(f"The square root of {num} is: {result}")
except NegativeNumberError as e:
    print("Error:", e)