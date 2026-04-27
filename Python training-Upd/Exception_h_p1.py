# exception handling in python
try:
    # code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
    print("The result is:", result)
except ZeroDivisionError as e:
    print("Error: You cannot divide by zero.")
    print("Exception message:", e)
except Exception as e:
    print("An unexpected error occurred:", e)