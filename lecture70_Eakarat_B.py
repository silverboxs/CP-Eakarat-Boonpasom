menuList = []
priceList = []

def showBill():
    print("----My Bill----")
    for x in range(len(menuList)):
        print((x+1),".",menuList[x]," @ ",priceList[x])
    print("-"*20)
    print("รวม :",sum(priceList),".-บาท")

while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Plese Enter Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()