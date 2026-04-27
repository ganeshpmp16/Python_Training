# dictionary.py
# Creating a dictionary
student = { "name": "Alice",
            "age": 25, 
            "grade": "A"
            }
print(student)
# Accessing values in a dictionary
print("Name:", student["name"])
print("Age:", student["age"])
print("Grade:", student["grade"])
# Adding a new key-value pair to the dictionary
student["major"] = "Computer Science"
print("Updated student dictionary:", student)
# Looping through the dictionary
print("Looping through the dictionary:")
for key, value in student.items():
    print(key + ":", value)
# Removing a key-value pair from the dictionary
del student["grade"]
print("Student dictionary after removing grade:", student)
