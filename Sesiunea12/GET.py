import requests

# GET - primeste date catre server
url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed - {response.status_code}")
