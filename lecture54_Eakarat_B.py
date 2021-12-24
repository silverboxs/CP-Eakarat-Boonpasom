def userLogin():
    usernameInput = input("Username :>>")
    passwordInput = input("Password :>>")
    if usernameInput == "admin" and passwordInput == "12345":
        return True;
    else:
         print("Login False..!!")

def productList():
    print("-------->Welcome Silverbox Shop <--------")
    print(">>1. RAM DDR4 16Gb 2666MHz @ 1,280.-THB")
    print(">>2. CPU intel Core i5 @ 7,880.-THB")
    print("Buy more than 5000 baht, get 5% discount.")
    print("-----------------------------------------")

def VAT_Calcute(price):
    print("VAT            : +",price * 0.07," .-THB")
    print("--------------------------------------")
    return price * 1.07

def Discount_Calcute(price):
    if price >= 5000:
        print("--------------------------------------")
        print("                    ",price,".-THB")
        print("Discount        : -",price * 0.05,".-THB")
        print("--------------------------------------")
        print("                  ",price * 0.95,".-THB")
        return price * 0.95
    else:
        print("--------------------------------------")
        print("                   ",price,".-THB")
        return price

def Price_Calcute(productPrice, ea):
    totalPrice = productPrice * ea
    totalPrice = Discount_Calcute(totalPrice)
    totalPrice = VAT_Calcute(totalPrice)
    return totalPrice

def cmSelect():
    PDchoose = input("Please select products 1 or 2 Enter :")
    if PDchoose == "1":
        print("Your choose >> RAM DDR4 16Gb 2666MHz")
        ea = int(input("Please enter amount :"))
        print("Total        : ",Price_Calcute(1280,ea),".-THB")
        #print(totalPrice)
    elif PDchoose == "2":
        print("Your choose >> RAM DDR4 16Gb 2666MHz")
        ea = int(input("Please enter amount :"))
        print("Total        : ",Price_Calcute(3480,ea),".-THB")
    else:
        print("You have selected the wrong product.")

### Main Program ###
if userLogin() == True:
    productList()   #<------ แสดงรายชื่อสินค้า
    cmSelect()      #<------ เรียกใช้ฟังก์ชั่นการทำงาน