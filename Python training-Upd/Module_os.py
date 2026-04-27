import os
# using the os module
current_directory = os.getcwd()
print("Current working directory:", current_directory)  # prints the current working directory
# list all files and directories in the current directory
files_and_directories = os.listdir(current_directory)
print("Files and directories in the current directory:", files_and_directories)  # prints a list of files and directories in the current directory
# create a new directory
new_directory = "python_training"
if not os.path.exists(new_directory):
    os.mkdir(new_directory)
    print(f"Directory '{new_directory}' created.")
# change the current working directory to the new directory
os.chdir(new_directory)
print("Current working directory after change:", os.getcwd())  # prints the new current working directory