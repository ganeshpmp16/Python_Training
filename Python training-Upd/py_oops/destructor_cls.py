# destruction demo 
class Employee:
    def __init__(self, name):
        self.name = name
        print(f"Employee {self.name} created.")
    def __del__(self): # __del__ is the destructor method in Python classes. It is automatically called when an instance of the class is about to be destroyed. The purpose of the __del__ method is to perform any necessary cleanup actions before the object is removed from memory. It can be used to release resources, close files, or perform any other necessary cleanup tasks. 
        print(f"Employee {self.name} destroyed.")   
# Example usage
employee1 = Employee("John")
employee2 = Employee("Jane")
print("End of the program.")
del employee1
del employee2
