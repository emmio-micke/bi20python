import json

# some JSON:
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# parse x:
#y = json.dumps(x, indent=4, separators=(";", " = "))
#y = json.dumps(x, indent=2, sort_keys=True)
y = json.dumps(x, indent=2)

# the result is a string:

print(y)
# print(type(y))
