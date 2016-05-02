import requests, re

def domenfinder(url, domains, regulars):
    result = url
    for ritem in regulars:
        result = re.sub(ritem, '', result)
    if result != '' and (result not in domains):
        domains.append(result)
#    for item in re.findall(r"href[\S]+[\"\'](.+)[\"\']", url):
#        result = re.sub(r"([\S]+[/]{2})", '', item)
#        result = re.sub(r"../(.+)", '', result)
#        print(result)
#        result = re.sub(r"((.)*/{2})", '', item)
#        result = re.sub(r"(.)*([/:]{1}.*)", '', result)
#        if result != '' and (result not in domains):
 #           domains.append(result)

#S = input()
#res = requests.get(S)
#if res.status_code != 200:
domains = []
regulars = [
    r"\"(.+)",
    r"\?(.+)",
    r"/$",
    r"(.+)://",
    r"\.*/(.+)",
    r":(.+)"
]
with open("test2") as f:
    res = f.read()
    urls = re.findall(r"[^\']<a.*?href=[\"\'](.*?)[\"\'].*?>", res)
    for url in urls:
        domenfinder(url, domains, regulars)
domains.sort()
for item in domains:
    print(item)