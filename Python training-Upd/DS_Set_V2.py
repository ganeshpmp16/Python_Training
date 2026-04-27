# remove duplicates from a list using a set
my_list = ["apple", "banana", "cherry", "apple", "banana"]
my_set = set(my_list)
print(my_set)  # prints {"apple", "banana", "cherry"}
# convert the set back to a list
unique_list = list(my_set)
print(unique_list)  # prints ["apple", "banana", "cherry"] (order may vary) 
