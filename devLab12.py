inputCode = input()
decodeList = list()
y = ""

for x in inputCode:
    if x.isdigit():
        y += x
    else:
        decodeList.append(y)
        y = ""

print(decodeList)