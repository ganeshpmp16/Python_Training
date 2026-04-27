# single inheritance example in Python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.subject = subject

    def display_info(self):
        super().display_info()  # Call the display_info method of the parent class
        print(f"Subject: {self.subject}")

# Example usage
teacher1 = Teacher("Mr. Smith", 40, "Mathematics")
teacher1.display_info()

