import requests, re

class Flag:
    def __init__(self, count=0):
         self.count = count
    def modifycount(self, count):
        self.count = max(count, self.count)
        return self
    def check(self):
        if self.count == 2:
            return True
        return False

def urlfinder(current, goal, flag, count=0, stop=False):
    if count > 2:
        return
    if current == goal:
        flag.modifycount(count)
    res = requests.get(current)
    if res.status_code != 200:
        return
    urls = re.findall(r"href=\"(.+)\"", res.text)
    for url in urls:
        urlfinder(url, goal, flag, count + 1)

A, B = (input() for i in range(2))
flag = Flag()
urlfinder(A, B, flag)
if flag.check():
    print("Yes")
else:
    print("No")