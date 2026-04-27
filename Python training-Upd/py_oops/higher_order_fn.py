# function passed as an argument to another function is called higher order function
def higher_order_function(func):
    print("This is a higher order function.")
    func() # call the passed function   

def say_hello():
    print("Hello, World!")
higher_order_function(say_hello)
# Output:
# This is a higher order function.
# Hello, World!
# we can also return a function from another function
def outer_function():
    print("This is the outer function.")
    def inner_function():
        print("This is the inner function.")
    return inner_function # return the inner function   
my_inner_function = outer_function() # call the outer function and get the inner function
my_inner_function() # call the inner function
# Output:
# This is the outer function.
# This is the inner function.
    
