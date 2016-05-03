import re

filename = "dataset_3363_2.txt"
with open("files/" + filename) as file:
    data = file.read()
with open("files/" + "_" + filename, 'w') as file:
    reg = re.findall(r"([a-zA-Z]{1}[0-9]+)", data)
    for item in reg:
        file.write(item[0] * int(item[1:]))
