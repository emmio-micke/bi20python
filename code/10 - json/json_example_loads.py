import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
z = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(x)
print(type(x))
# print(type(z))

# parse x:
y = json.loads(x)

# the result is a Python dictionary:

print(y)
print(type(y))
print(y["age"])
