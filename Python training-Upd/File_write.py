import os
# creat a new file and write to it
file_name = "example_file.txt"
with open(file_name, 'w') as file:
    file.write("This is an example of writing to a file in Python.\n")
    file.write("You can write multiple lines to the file.\n")
    file.write("This file is created using the 'with' statement, which ensures proper resource management.")    
print(f"File '{file_name}' has been created and written to.")