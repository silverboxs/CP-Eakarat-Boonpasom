menuList = []
totalPrice = []

def showBill():
    print("----My Bill----")
    for x in range(len(menuList)):
        print((x+1),".",menuList[x][0]," @ ",menuList[x][1])
    print("-"*20)    
    #print("รวม :",sum(menuList[1]),".-บาท")


while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Plese Enter Price : "))
        menuList.append([menuName,menuPrice])
        #priceList.append(menuPrice)

showBill()