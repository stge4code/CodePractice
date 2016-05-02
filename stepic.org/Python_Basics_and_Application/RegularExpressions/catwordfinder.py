import sys, re
#result = []
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\bcat\b"
    if len(re.findall(pattern, line)) > 0:
#        result.append(line)
        print(line)
#print(result)