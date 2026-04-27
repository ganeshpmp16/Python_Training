#variables
name = "John"
age = 30
salary = 50000.0
print("Name:", name)
print("Age:", age)
print("Salary:", salary)
#data types
name = "Alice"  # string
age = 25  # integer
height = 1.75  # float
is_student = True  # boolean
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

#Type checking
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))  
print("Type of is_student:", type(is_student))

#type conversion
age_str = str(age)  # Convert integer to string
height_int = int(height)  # Convert float to integer
is_student_str = str(is_student)  # Convert boolean to string
print("Age as string:", age_str)
print("Height as integer:", height_int)
print("Is Student as string:", is_student_str)

#input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello, " + name + "! You are " + str(age) + " years old.")

