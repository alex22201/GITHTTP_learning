import requests


link = "http://omwap.mywibes.com/brouser_info/"
responce = requests.get(link).text

print(responce)
with open("./1.html", "w", encoding="utf-8") as file:
    file.write(responce)
))))