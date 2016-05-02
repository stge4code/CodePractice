filename = "dataset_24465_4.txt"
with open(filename) as file:
    data = file.read().splitlines()
data.reverse()
for item in data:
    print(item)