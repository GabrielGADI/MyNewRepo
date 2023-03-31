import requests

# PATCH - actualizeaza o parte din sursa
url = "https://jsonplaceholder.typicode.com/posts/1"

payload = {
    "title": "foo"
}
response = requests.patch(url, json=payload)  # va modifica ce este specificat in payload

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"request failed - {response.status_code}")

# spre deosebire de PUT, PATCH actualizeaza doar campurile care apar in payload
