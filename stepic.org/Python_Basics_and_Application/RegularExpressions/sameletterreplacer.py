import sys, re
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"(\w)\1+"
    print(re.sub(pattern, r"\1", line))