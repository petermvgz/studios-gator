import json

data = '''
{
  "name" : "Peter",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "peterdeyi@gmail.com"
   }
}'''

info = json.loads(data)
# loads = load from string
# info = dictionary
print('Name:', info["name"])
print('hide:', info["email"]["hide"])
# JSON represents data as nested "lists" and "dictionaries"
