import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

# Get Request
response = requests.get(api_url)

print(response.json())  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}

print(response.status_code)  # 200
print(response.headers["Content-Type"])  # application/json; charset=utf-8


# POST request
todo = {"userId": 1, "title": "Buy milk", "completed": False}

response = requests.post(api_url, json=todo)

print(response.json()) # {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

print(response.status_code) # 200


# Put Request
todo = {"title": "Mow lawn"}
response = requests.put(api_url, json=todo)
print(response.json)
print(response.status_code)





