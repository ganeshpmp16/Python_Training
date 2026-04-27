# contructor with default value
class Employee:
    def __init__(self, name, age=30):
        self.name = name
        self.age = age
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
# Example usage
employee1 = Employee("John")
employee1.display_info()
employee2 = Employee("Jane", 25)
employee2.display_info()
