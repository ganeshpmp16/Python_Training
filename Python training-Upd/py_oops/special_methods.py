# Special Methods in Python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})" #provides a human-readable string representation of the object, often used for display purposes.

    def __repr__(self): #provides a more detailed and unambiguous string representation of the object, often used for debugging and development purposes.
        return f"Student(name='{self.name}', age={self.age})"

    def __eq__(self, other): #overriding the equality operator to compare two Student objects based on their attributes 
        if isinstance(other, Student): # other means the object we are comparing with, and we check if it is an instance of the Student class. If it is, we compare their name and age attributes for equality. If both attributes are equal, we return True; otherwise, we return False. If the other object is not an instance of Student, we return False.
            return self.name == other.name and self.age == other.age
        return False
    
student1 = Student("Alice", 20)
student2 = Student("Alice", 40)
print(student1)  # Output: Student(name=Alice, age=20)
print(repr(student1))  # Output: Student(name='Alice', age=40)
print(student1 == student2)  # Output: True
