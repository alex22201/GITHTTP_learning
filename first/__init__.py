import requests

headers = {
    "User-Agent": "Glolooooololo"
}
response = requests.post("http://httpbin.org/post", headers=headers,
                        params={'a': 'b', 'c': 10},
                        json={'username': 'supersecret'})
if response.ok:
    print("ok!")
print(response.text)
# print(response.json()['headers']['User-Agent'])
