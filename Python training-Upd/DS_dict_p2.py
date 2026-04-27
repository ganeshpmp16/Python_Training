# important methods of dict
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
# get() method to access values
print(my_dict.get("name"))  # prints "Alice"
print(my_dict.get("age"))   # prints 30
print(my_dict.get("city"))  # prints "New York"
# keys() method to get all keys
print(my_dict.keys())  # prints dict_keys(['name', 'age', 'city'])
# values() method to get all values
print(my_dict.values())  # prints dict_values(['Alice', 30, 'New York'])
# items() method to get all key-value pairs
print(my_dict.items())  # prints dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])
