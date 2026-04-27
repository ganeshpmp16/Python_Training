# multi level inheritance example in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info() # Call the display_info method of the parent class which is  Person class    
        print(f"Employee ID: {self.employee_id}")

class Manager(Employee):
    def __init__(self, name, age, employee_id, department):
        super().__init__(name, age, employee_id)
        self.department = department

    def display_info(self):
        super().display_info() # Call the display_info method of the parent class which is Employee class   
        print(f"Department: {self.department}") 
# Example usage
manager1 = Manager("Alice", 35, "E123", "Sales")
manager1.display_info()

