# decorator sample decorator is a function that takes another function as an argument and extends the behavior of the latter function without explicitly modifying it.
def decorator(func): # 
    def wrapper(): # wrapper function that will be returned by the decorator
        print("Before the function call")
        result = func() # call the original function
        print("After the function call")
        return result
    return wrapper

@decorator
def say_hello():
    print("Hello, World!")

say_hello()
