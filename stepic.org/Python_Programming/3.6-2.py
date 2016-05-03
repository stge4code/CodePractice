import requests
filename = "dataset_3378_2.txt"
with open("files/" + filename) as file:
    url = file.readline().strip()
res = requests.get(url)
result = []
for item in res.text.splitlines():
    if item != '':
        result.append(item)
print(len(result), len(res.text.splitlines()))
#print(res.text)