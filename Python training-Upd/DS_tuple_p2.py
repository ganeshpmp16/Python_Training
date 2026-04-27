# loop tuple inside a dictionary
students = {
    "Ramesh": (90, "Pass"),
    "Suresh": (85, "Pass"),
    "Akash": (45, "Fail")
}
for name, (score, status) in students.items():
    print(f"{name} scored {score} and is {status}.")
# prints "Ramesh scored 90 and is Pass.", "Suresh scored 85 and is Pass.", "Akash scored 45 and is Fail." on separate lines
# employee data with tuple values
employees = {
    "Alice": ("HR", 50000),
    "Bob": ("Engineering", 70000),
    "Charlie": ("Marketing", 60000)
}
for name, (department, salary) in employees.items():
    print(f"{name} works in {department} and earns ${salary}.")
# prints "Alice works in HR and earns $50000.", "Bob works in Engineering and earns $70000.", "Charlie works in Marketing and earns $60000." on separate lines
employee_data = (

    ("Alice", "HR", 50000),
    ("Bob", "Engineering", 70000),
    ("Charlie", "Marketing", 60000)
)
for name, department, salary in employee_data:
    print(f"{name} works in {department} and earns ${salary}.")
# prints "Alice works in HR and earns $50000.", "Bob works in Engineering and earns $70000.", "Charlie works in Marketing and earns $60000." on separate lines  
