import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)
print(response.json())  # {'userId': 1, 'id': 1, 'title': 'delectus aut autem', 'completed': False}
print(response.status_code)  # 200
print(response.headers["Content-Type"])  # application/json; charset=utf-8

todo = {"userId":1, "title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json() # {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}
response.status_code # 200



