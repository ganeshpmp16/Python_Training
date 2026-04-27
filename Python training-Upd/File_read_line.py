# read a file line by line
import os
folder = r"D:/Python training-Upd/py_files"
file_path = os.path.join(folder, "data2.txt")
try:
    with open(file_path, 'r') as file:
        print("Contents of the file:")
        for line in file:
            print(line, end='')  # end='' to avoid adding extra new line
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
