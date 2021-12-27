menuList = []
totalPrice = []
menuOrder = {
    'ข้าวมันไก่':35,
    'ข้าวหมูแดง': 40,
    'ข้าวหมูกรอบ': 45
}

def showBill():
    print("----My Bill----")
    for x in range(len(menuList)):
        print((x+1),".",menuList[x][0]," @ ",menuList[x][1])
    print("-"*20)    
    print("รวม :",sum(totalPrice),".-บาท")


while True:
    menuName = input("Plese Enter Menu : ")
    if(menuName.lower() == "exit"):
        break
    elif menuName in menuOrder:
        menuList.append([menuName,menuOrder[menuName]])
        totalPrice.append(menuOrder[menuName])
    else:
        print("Oop!! We don't have a menu for your choice. ")
        print("-"*10," My Menu ","-"*10)
        for x in menuOrder.keys():
            print("-",x," ราคา:",menuOrder[x],".-บาท")
showBill()

