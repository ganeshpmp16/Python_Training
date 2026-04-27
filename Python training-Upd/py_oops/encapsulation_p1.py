# usage of public members in encapsulation
class Employee:
    def __init__(self, name, age):
        self.name = name  # public member
        self.age = age    # public member

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


emp1 = Employee("Alice", 30)
emp1.display_info()  # Output: Name: Alice, Age: 30
# Accessing public members directly
print(emp1.name)  # Output: Alice
print(emp1.age)   # Output: 30
