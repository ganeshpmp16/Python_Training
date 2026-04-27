
# __init__ is the constructor method in Python classes. It is automatically called when a new instance of the class is created. The purpose of the __init__ method is to initialize the attributes of the class with the values provided when creating an instance. The self parameter is a reference to the current instance of the class, and it is used to access the attributes and methods of the class.
class Student:
    def __init__(self, name, age):# self is a reference to the current instance of the class, and it is used to access the attributes and methods of the class.
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")    
        
# Example usage
student1 = Student("Alice", 20)
student1.display_info()
student2 = Student("Bob", 22)
student2.display_info()
