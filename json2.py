import json

data = '''
[
  { "id" : "001",
    "x" : "23",
    "name" : "Peter"
  } ,
  { "id" : "009",
    "x" : "20",
    "name" : "Elissa"
  }
]'''
# List of two dictionaries
info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])
