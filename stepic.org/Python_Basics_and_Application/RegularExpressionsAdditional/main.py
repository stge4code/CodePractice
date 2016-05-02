import sys, re

def auto_graph(pos, levelvalue):
    if pos == 0:
        if levelvalue == '0':
            return 0
        else:
            return 1
    if pos == 1:
        if levelvalue == '1':
            return 0
        else:
            return 2
    if pos == 2:
        if levelvalue == '0':
            return 1
        else:
            return 2

for line in sys.stdin:
    line = line.rstrip()
#    for level0 in re.findall(r"^([01]+)$", line):
#        count = 0
#        for level1 in re.findall(r"([01]{1,2})", level0[::-1]):
#            level2 = level1[::-1]
#            if len(level2) == 1:
#                level2 = '0' + level2
#            if level2 == "10":
#                count -= 1
#            if level2 == "01":
#                count += 1
#        if count == 0:
#            print(line)
    for level0 in re.findall(r"^([01]+)$", line):
        pos = 0
        for level1 in re.findall(r"([01]{1})", '0' + level0):
            pos = auto_graph(pos, level1)
        if pos == 0:
            print(line)