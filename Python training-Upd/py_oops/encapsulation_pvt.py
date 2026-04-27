# private variables and methods in python are denoted by prefixing the name with double underscores (__)
class Employee:
    def __init__(self, name, age):
        self.__name = name  # private member
        self.__age = age    # private member

    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

    def __private_method(self):
        print("This is a private method.")
emp1 = Employee("Alice", 30)

emp1.display_info()  # Output: Name: Alice, Age: 30
# Accessing private members directly will raise an AttributeError
#print(emp1.__name)  # This will raise an error
# Accessing private method directly will also raise an AttributeError
# emp1.__private_method()  # This will raise an error
# However, private members can be accessed using name mangling
print(emp1._Employee__name)  # Output: Alice
print(emp1._Employee__age)   # Output: 30
emp1._Employee__private_method()  # Output: This is a private method.
