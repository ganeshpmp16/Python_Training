# multiple inheritance example in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        
class Employee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

    def display_employee_info(self):
        print(f"Employee ID: {self.employee_id}")
class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, department):
        Person.__init__(self, name, age)  # Call the constructor of the Person class
        Employee.__init__(self, employee_id)  # Call the constructor of the Employee class
        self.department = department

    def display_info(self):
        Person.display_info(self)  # Call the display_info method of the Person class
        Employee.display_employee_info(self)  # Call the display_employee_info method of the Employee class
        print(f"Department: {self.department}")
# Example usage
manager1 = Manager("Alice", 35, "E123", "Sales")
manager1.display_info()
