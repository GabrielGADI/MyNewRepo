import requests

# PUT - actualizeaza si inlocuieste intreaga resursa cu payload dat de noi
url = "https://jsonplaceholder.typicode.com/posts/1"  # update se face pe o singura resursa

payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.put(url, json=payload)  # inlocuieste intreaga resursa

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"request failed - {response.status_code}")
