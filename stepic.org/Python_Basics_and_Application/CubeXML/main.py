from xml.etree import ElementTree
class Color:
    def __init__(self, name):
        self.price = 0
        self.name = name
    def incrprice(self, value=1):
        self.price += value

class Colors(dict):
    def __init__(self):
        super(dict, self).__init__()
        self["red"] = Color("red")
        self["blue"] = Color("blue")
        self["green"] = Color("green")

    def getcolor(self, colorname, colorprice=0):
        if colorname not in self:
            color = Color(colorname)
            self[color.name] = color
        result = self[colorname]
        result.incrprice(colorprice)
        return result


class Cube:
    def __init__(self, color, price):
        self.childs = []
        self.price = price
        self.color = color
    def addchild(self, cube):
        self.childs.append(cube)

class Piramid(list):

    def addlevel(self, cube):
        self.append(cube)

def treewalker(piramid, colors, element, cubeprice=1):
    color = colors.getcolor(element.attrib["color"].strip(), cubeprice)
    cube = Cube(color, cubeprice)
    piramid.addlevel(cube)
    for item in element:
        cube.addchild(treewalker(piramid, colors, item, cubeprice + 1))
    return cube

colors = Colors()
piramid = Piramid()


treewalker(piramid, colors, ElementTree.parse("tree").getroot())
#treewalker(piramid, colors, ElementTree.fromstring(input()))

print(colors["red"].price, colors["green"].price, colors["blue"].price, sep=' ')

#for item in colors:
#    print(colors[item].price, end=' ')