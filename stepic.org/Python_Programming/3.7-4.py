# put your python code here
class Turtle:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def movement(self, s):
        (cmd, steps) = (s.split())
        self.CMDs[cmd](self, int(steps))

    def nord(self, steps):
        self.y += steps

    def east(self, steps):
        self.x += steps

    def west(self, steps):
        self.x -= steps

    def south(self, steps):
        self.y -= steps

    def getcoords(self):
        return str(self.x) + ' ' + str(self.y)

    CMDs = {
        "север": nord,
        "юг": south,
        "восток": east,
        "запад": west
    }


turtle = Turtle()
n = int(input())
for i in range(n):
    turtle.movement(input())
print(turtle.getcoords())