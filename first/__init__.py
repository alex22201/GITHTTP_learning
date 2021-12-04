import requests

headers = {
    "User-Agent": "Glolooooololo"
}
response = requests.get("http://httpbin.org/get", headers=headers)

if response.ok:
    print("ok!")
print(response.text)
print(response.json()['headers']['User-Agent'])