import json

with open('data.json') as json_data:

    json_data = json_data.read()
    data = json.loads(json_data)

    print(data)

    print(data['employees'])
    print(data['employees']['name'])
    print(data['employees']['company'])

    print(type(json_data))
    print(type(data))
