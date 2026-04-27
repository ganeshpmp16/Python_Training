# exception handling in python using else block
try:
    # code that may raise an exception
    result = 10 / 2  # This will not raise an exception
    print("The result is:", result)
except ZeroDivisionError as e:
    print("Error: You cannot divide by zero.")
    print("Exception message:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
else:
    print("The operation was successful, and no exceptions were raised.")