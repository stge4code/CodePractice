import sys, re
for line in sys.stdin:
    line = line.rstrip()
    pattern = r"\b([aA]+)\b"
    print(re.sub(pattern, "argh", line, count=1))
