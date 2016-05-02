import requests, re


def domenfinder(url, domains, regulars):
    result = url
    for ritem in regulars:
        result = re.sub(ritem, '', result)
    if result != '' and (result not in domains):
        domains.append(result)

S = input()
res = requests.get(S)
domains = []
regulars = [
    r"\"(.+)",
    r"\?(.+)",
    r"/$",
    r"(.+)://",
    r"\.*/(.+)",
    r":(.+)"
]
urls = re.findall(r"[^\']<a.*?href=[\"\'](.*?)[\"\'].*?>", res.text)
for url in urls:
    domenfinder(url, domains, regulars)
domains.sort()
for item in domains:
    print(item)