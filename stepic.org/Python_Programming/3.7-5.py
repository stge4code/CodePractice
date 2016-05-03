class Puple():
    def __init__(self, group, name, height):
        self.group = int(group)
        self.name = name
        self.height = int(height)

class Group(list):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.height = 0
        self.numbers = 0
    def append(self, p_object):
        if p_object not in self:
            super().append(p_object)
            self.height += p_object.height
            self.numbers += 1
    def gehmeanheight(self):
        if self.numbers == 0:
            return '-'
        return self.height / self.numbers

class Pool(dict):
    def __init__(self):
        super().__init__()
        for i in range(1, 12):
            groupname = str(i)
            self[groupname] = Group(groupname)
    def getgroup(self, groupname):
        return  self[groupname]

    def printgroups(self):
        for key in sorted(self, key=lambda x:int(x)):
            print(self.getgroup(key).name, self.getgroup(key).gehmeanheight(), sep=' ')

filename = "dataset_3380_5.txt"
with open("files/" + filename) as file:
    data = file.read().splitlines()
pool = Pool()
for line in data:
    tmp = line.split()
    pool.getgroup(tmp[0]).append(Puple(tmp[0],  tmp[1],  tmp[2]))

pool.printgroups()
