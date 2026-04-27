# to create file and directory
import os
# using the os module
current_directory = os.getcwd()
print("Current working directory:", current_directory)  # prints the current working directory
# create a new directory
new_directory = "py_training_files"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created.")
# change the current working directory to the new directory
os.chdir(new_directory)
print("Current working directory after change:", os.getcwd())  # prints the new current working directory
# create a new file in the new directory
new_file = "example.txt"
with open(new_file, 'w') as file:
    file.write("This is an example file created using the os module.")  
print(f"File '{new_file}' created in directory '{new_directory}'.")
