import requests
import json

client_id = "77c78c2b881a3d231f07"
client_secret = "cda04ea9a6cec4f1ff4b9df13a303283"


# инициируем запрос на получение токена
gettoken = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# достаем токен
token = json.loads(gettoken.text)["token"]
# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}

filename = "dataset_24476_4.txt"
# инициируем запрос с заголовком
artistslist = {}

with open(filename, encoding="UTF-8") as file:
    for artist in file.read().split():
        url = "https://api.artsy.net/api/artists/" + artist
        getdata = requests.get(url, headers=headers)
        getdata.encoding = "UTF-8"
        data = json.loads(getdata.text)
        date = data["birthday"]
#        name = data["sortable_name"].encode(encoding="UTF-8", errors="strict")
        name = data["sortable_name"]
        if date not in artistslist:
            artistslist[date] = []
        artistslist[date].append(name)
for key in artistslist:
    artistslist[key].sort()
result = []
keys = sorted(artistslist)
for key in keys:
    for name in artistslist[key]:
        result.append(name)
        print(name)
with open("_" + filename,  "w", encoding="UTF-8") as file:
    for item in result:
        file.write(item + "\n")
