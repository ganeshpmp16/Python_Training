# using static method to create a method that does not depend on the instance or class variables
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b
    
# Using the static methods without creating an instance of the class
result1 = MathUtils.add(5, 3)
result2 = MathUtils.multiply(5, 3)
print(f"Addition: {result1}")       # Output: Addition: 8
print(f"Multiplication: {result2}")  # Output: Multiplication: 15
