import os
import os.path

for dir, in_dirs, in_files in os.walk("main"):
    flag = False
    for file in in_files:
        if ".py" in file:
            flag = True
    if flag:
        print(dir)