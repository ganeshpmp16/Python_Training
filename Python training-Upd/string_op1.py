# string handling in Python
# creating a string
my_string = "Hello, World!"
print(my_string)  # prints "Hello, World!"
# string concatenation
greeting = "Hello"
name = "Alice"
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # prints "Hello, Alice!"          
# string formatting
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string)  # prints "Alice is 30 years old."
# string methods
print(my_string.upper())  # prints "HELLO, WORLD!"
print(my_string.lower())  # prints "hello, world!"
print(my_string.replace("World", "Python"))  # prints "Hello, Python!"  
print(my_string.split(", "))  # prints ["Hello", "World!"]
# joining a list of strings
words = ["Hello", "Python", "Programming"]
joined_string = " ".join(words)
print(joined_string)  # prints "Hello Python Programming"
#startwith and endswith
print(my_string.startswith("Hello"))  # prints True
print(my_string.endswith("!"))  # prints True
# f-strings with expressions
a = 5
b = 10
result_string = f"The sum of {a} and {b} is {a + b}."
print(result_string)  # prints "The sum of 5 and 10 is 15."
#check string contents
print(my_string.isalpha())  # prints False (because of spaces and punctuation)
print("Hello".isalpha())  # prints True
print(my_string.isdigit())  # prints False
print("12345".isdigit())  # prints True
print(my_string.isspace())  # prints False
print("   ".isspace())  # prints True
# loop through characters in a string
for char in my_string:
    print(char)
# prints each character of "Hello, World!" on a separate line   
