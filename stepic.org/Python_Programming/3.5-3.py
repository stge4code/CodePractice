import sys
for item in sys.argv:
    if sys.argv.index(item) > 0:
        print(item, sep=' ')