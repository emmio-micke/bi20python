import requests
import json

response = requests.get("https://randomuser.me/api")
#response = requests.get("https://randomuser.me")

# print(response.text)

data = response.json()

print(data["results"][0]["location"]["country"])

# print(data["results"][0]["name"]["first"])
# print(data["results"][0]["name"]["last"])
# print(data)
# print(type(data))
