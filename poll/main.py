import requests

# Get API Request

api_url = 'https://jsonplaceholder.typicode.com/todos/1'
response = requests.get(api_url)
# print(response.json())

# POST

api_url = "https://jsonplaceholder.typicode.com/todos"
todo = {"userId": 1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
# print(response.status_code)

# PUT

api_url = "https://jsonplaceholder.typicode.com/todos/10"
todo = {"userId": 1, "title": "Wash car", "completed": True}
response = requests.put(api_url, json=todo)
print(response.status_code)

# Delete

api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.status_code)

