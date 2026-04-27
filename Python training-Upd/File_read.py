# to read the contents of a file
import os
folder = r"D:/Python training-Upd/py_files"
file_path = os.path.join(folder, "data.txt")
try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
    
