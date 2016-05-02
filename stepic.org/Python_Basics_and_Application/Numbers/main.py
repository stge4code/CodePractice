import requests

def info(number):
    url = "http://numbersapi.com/" + str(number) + "/math"
    boringlist = [
        "unremarkable",
        "boring",
        "missing a fact",
        "uninteresting"
    ]
    params = {
        "json":"true"
    }
    result = requests.get(url, params=params).json()
    for item in boringlist:
        if item in result["text"]:
            return "Boring"
    return "Interesting"
filename = "dataset_24476_3.txt"
with open(filename) as file:
    numbers = file.read().split()
    for number in numbers:
        print(info(number))
