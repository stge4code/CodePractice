import sys, re
#result = []
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"cat"
    if len(re.findall(pattern, line)) > 1:
#        result.append(line)
        print(line)
#print(result)