import csv
def finder(x):
    if (x[2].split('/')[2] == "2015"):
        return x[5]
    return ''

with open("Crimes.csv") as f:
    reader = csv.reader(f)
#    print(reader.__next__())
    print(max(reader, key=finder)[5])
