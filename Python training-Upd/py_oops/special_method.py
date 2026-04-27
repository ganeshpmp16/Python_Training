# len special method
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
    
my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5
# str special method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
person = Person("Alice", 30)
print(person)  # Output: Person(name=Alice, age=30)

# add special method
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        return NotImplemented
    
num1 = Number(5)
num2 = Number(10)
result = num1 + num2
print(result.value)  # Output: 15

