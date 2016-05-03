d = int(input())
correctwords = [input().lower() for i in range(d)]
l = int(input())
text = [input().split() for i in range(l)]
result = []
for line in text:
    for item in line:
        temp = item.lower()
        if temp not in correctwords:
            if temp not in result:
                result.append(temp)
print('\n'.join(result))