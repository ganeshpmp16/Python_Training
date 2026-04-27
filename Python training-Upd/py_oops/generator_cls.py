# generator is a function which return an iterator object which we can iterate one value at a time
def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()

print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3
# using for loop to iterate through the generator
for value in my_generator():
    print(value)  # Output: 1 2 3

# using generator expression to create a generator
squares = (x**2 for x in range(5))
for square in squares:
    print(square)  # Output: 0 1 4 9 16

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Example usage
for num in fibonacci(10):
    print(num)  # Output: 0 1 1 2 3 5 8 13 21 34    

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
# Example usage
for number in count_up_to(5):
    print(number)  # Output: 1 2 3 4 5
def SquareGenerator(n):
    for i in range(n):
        yield i**2 
# Example usage
for square in SquareGenerator(5):
    print(square)  # Output: 0 1 4 9 16
