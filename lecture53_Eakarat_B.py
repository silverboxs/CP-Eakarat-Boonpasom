def vatCal(price):
    totalPrice = price * 1.07
    return totalPrice

productPrice = float(input("Insert Price : "))
print(vatCal(productPrice))
