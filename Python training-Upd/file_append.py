# append to a given file
import os
folder = r"D:/Python training-Upd/py_files"
file_path = os.path.join(folder, "data.txt")
try:
    with open(file_path, 'a') as file:  # 'a' mode for appending
        file.write("This line is appended to the file.\n")
        file.write("Appending allows you to add content without overwriting existing data.\n")
    print(f"Content has been appended to '{file_path}'.")
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")