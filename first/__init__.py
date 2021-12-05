import requests

#headers = {
#    "User-Agent": "Glolooooololo"
#}
#responce = requests.post("http://httpbin.org/post", headers=headers,
#                       params={'a': 'b', 'c': 10},
#                       json={'username': 'supersecret'})

link = "http://omwap.mywibes.com/brouser_info/"
responce = requests.get(link).text

print(responce)
with open("./1.html", "w", encoding="utf-8") as file:
    file.write(responce)
#print(responce.text)
# print(responce.json()['headers']['User-Agent'])
