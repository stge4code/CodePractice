filename = "dataset_3363_4.txt"
math = 0
phys = 0
lang = 0
count = 0
with open("files/" + filename) as file:
    result = []
    for item in file:
        S = item.split(';')
        if len(S) > 1:
            result.append(str((int(S[1]) + int(S[2]) + int(S[3])) / 3.0))
            math += int(S[1])
            phys += int(S[2])
            lang += int(S[3])
            count += 1
with open("files/" + '_'+ filename, 'w') as file:
    for item in result:
        file.write(item + '\n')
    file.write(str(math / count) + ' ' + str(phys / count) + ' ' + str(lang / count))