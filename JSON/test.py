import json

data = {
  "employee": {
    "name": "Sakib Al Hasan",
    "company": "SQUARE"
  }
}

# Python to JSON

# json_str = json.dumps(data)
json_str = json.dumps(data, indent=4)
# json_str = json.dumps(data, indent=4, sort_keys=True)
# json_str = json.dumps(data, indent=4, sort_keys=True, separators=(". ", " = "))

print(data['employee'])
print(data["employee"]["name"])
print(data["employee"]["company"])

print(data)
print(json_str)

print(type(data))
print(type(json_str))
