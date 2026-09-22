# A Program to convert Python data into JSON and back

import json

student = {
    "name": "Hasher",
    "age": 20,
    "course": "Information Technology"
}

json_data = json.dumps(student)

print("JSON data:")
print(json_data)

python_data = json.loads(json_data)

print("\nPython data:")
print(python_data)
print("Student name:", python_data["name"])

# Explanation:
# JSON is commonly used to store and exchange structured data.
# dumps() converts Python data into a JSON string.
# loads() converts a JSON string back into Python data.
# The resulting dictionary can then be accessed normally.

# Real-Life Use:
# JSON is widely used in APIs, configuration files, web applications, and communication between software systems.