amount = int(input())
productList = list()
result = list()

for rows in range(amount):
    PDID = int(input())
    productList.append(PDID)

IDinput = int(input())
for x in range(len(productList)):
    if productList[x] == IDinput:
        result.append(x+1)