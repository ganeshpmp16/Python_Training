import os
folder = r"D:/Python training-Upd/py_files"
os.makedirs(folder, exist_ok=True) # Create the folder if it doesn't exist
file_path = os.path.join(folder, "data.txt")
with open(file_path, 'w') as file:
    file.write("This is an example of writing to a file in Python.\n")
    file.write("You can write multiple lines to the file.\n")
    file.write("This file is created using the 'with' statement, which ensures proper resource management.")    
print(f"File '{file_path}' has been created and written to.")