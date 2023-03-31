import requests

# POST - trimite date catre server
url = "https://jsonplaceholder.typicode.com/posts"  # update-ul se face pe toate sursele deodata

payload = {  # date pe care le trimim numite payload
    "title": "foo",
    "body": "bar",
    "userID": 1
}

response = requests.post(url, json=payload)

if response.status_code == 201:  # code 201 vine de la created inlocuind code 200
    data = response.json()
    print(data)
else:
    print(f"Request failed - {response.status_code}")
