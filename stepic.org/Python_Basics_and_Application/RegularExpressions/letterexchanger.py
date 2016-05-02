import sys, re
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b(\w)(\w)(\w*)\b"
    print(re.sub(pattern, r"\2\1\3", line))
