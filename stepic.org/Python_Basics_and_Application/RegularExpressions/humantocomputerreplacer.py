import sys, re
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"human"
    print(re.sub(pattern, "computer", line))
