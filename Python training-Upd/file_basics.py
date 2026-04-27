# using open() to create and write to a file
# open() function is used to open a file in a specific mode (e.g., 'w' for writing, 'a' for appending, 'r' for reading)
# when you open a file in 'w' mode, it creates the file if it doesn't
# exist, or overwrites it if it does exist
import os
file = open("example.txt", 'w')  # 'w' mode for writing
file.write("This is an example of writing to a file in Python.\n")
file.write("You can write multiple lines to the file.\n")
file.write("This file is created using the open() function, which requires you to manually close the file after writing.")
file.close()  # Don't forget to close the file after writing    
print("File 'example.txt' has been created and written to.")

