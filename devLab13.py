amount = int(input())
productList = list()
result = list()
txt = ""

for rows in range(amount):
    PDID = int(input())
    productList.append(PDID)

IDinput = int(input())
for x in range(len(productList)):
    if productList[x] == IDinput:
        result.append(x+1)

txt = "Position:"+str(result[0])
print(result)
for l in range(len(result)):
    if l == 0:
        continue
    txt += ","+str(result[l])

print("Position: ",txt)
