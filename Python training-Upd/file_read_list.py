# read all the lines of a file into a list
import os
folder = r"D:/Python training-Upd/py_files"
file_path = os.path.join(folder, "data.txt")
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()  # read all lines into a list
        print("Lines in the file:")
        for line in lines:
            print(line, end='')  # end='' to avoid adding extra new line
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")