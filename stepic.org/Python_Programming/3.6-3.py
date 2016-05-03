import requests, re

filename = "dataset_3378_3.txt"
with open("files/" + filename) as file:
    url = file.readline().strip()
fileurl = re.findall(r"([^/]+)$", url)[0]
mainurl = re.sub(fileurl, '', url)
print(mainurl, fileurl, sep='\n')
while "We" not in fileurl:
    url = mainurl + fileurl
    res = requests.get(url)
    fileurl = res.text
print(fileurl)