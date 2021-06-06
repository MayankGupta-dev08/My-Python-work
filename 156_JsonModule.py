'''
JSON MODULE - JAVA SCRIPT OBJECT NOTATION, JSON is a syntax for storing and exchanging data.
JSON is text, written with JavaScript object notation.
JSON FILE IS STORED WITH .json extension
json file doesn't contain comments, its stored using '{}'

import json
json.loads() - If you have a JSON string, you can parse it by using the json.loads() method. The result will be a Python dictionary. Converting json to python.
json.load() - It is used to read the json documents from the file.
json.dump() - Converting python to json

When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python                  JSON
dict	                Object
list	                Array
tuple	                Array
str	                    String
int	                    Number
float	                Number
True	                true
False	                false
None	                null

'''
import json

# 1.  Converting Json to Python
data = '{"var1": "Harry", "var2": "Mannu", "var3": 98 }'
# data is basically a string written in json format
print(type(data))
print(data)
# print(data["var1"]) #this will give error as data is a string.

parsed = json.loads(data)
print(parsed)
print(type(parsed))
print(parsed["var1"], "\n\n")


# 2.  Convert a Python object containing all the legal data types:
import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

jscompatible1 = json.dumps(x, indent=4)
print(jscompatible1)
print(type(jscompatible1))
jscompatible2 = json.dumps(x, indent=4, separators=(". ", " = "))
print(jscompatible2)
jscompatible3 = json.dumps(x, indent=4, sort_keys=True)
print(jscompatible3)
