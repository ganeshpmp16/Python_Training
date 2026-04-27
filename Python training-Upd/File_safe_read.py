# safe file reading without error handling
import os
folder = r"D:/Python training-Upd/py_files"
file_path = os.path.join(folder, "data.txt")
if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
        print("Contents of the file:")
        print(contents)
else:
    print(f"File '{file_path}' not found.")

