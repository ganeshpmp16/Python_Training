# exception handling in python using finally block in file operations
try:
    file= open("example_file.txt", 'r')
    contents = file.read()
    print("Contents of the file:")
    print(contents)
except FileNotFoundError:
    print("Error: The file 'example_file.txt' was not found.")
except Exception as e:
    print("An unexpected error occurred:", e)
finally:
    if 'file' in locals(): # locals() checks if 'file' variable exists in the local scope   
        file.close()
        print("File has been closed.")  