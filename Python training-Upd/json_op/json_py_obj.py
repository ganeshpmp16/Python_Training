# python objec to json string
import json
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student = Student("Alice", 20)
# convert to json string
json_str = json.dumps(student.__dict__) #dumps() method can only serialize basic data types, so we need to convert the object to a dictionary first
print(json_str)

# json string to python object
json_str = '{"name": "Alice", "age": 20}'
student = json.loads(json_str) #loads() method returns a dictionary, so we can access the values using the keys 
print(student)

# json string to python object with custom class
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
def student_decoder(obj):
    return Student(obj['name'], obj['age'])

json_str = '{"name": "Alice", "age": 20}'
student = json.loads(json_str, object_hook=student_decoder) #object_hook parameter allows us to specify a custom function to decode the JSON string into a Python object
print(student.name)
print(student.age)
