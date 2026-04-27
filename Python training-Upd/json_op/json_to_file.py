# writing json data to file
import json
data = {
    "name": "Alice",
    "age": 20,
    "city": "New York"
}
with open('data.json', 'w') as file:
    json.dump(data, file) #dump() method writes the JSON data to a file where file represents the file object and data is the Python object to be serialized
# reading json data from file
with open('data.json', 'r') as file: 
  data = json.load(file) #load() method reads the JSON data from a file and returns a Python object
print(data)

