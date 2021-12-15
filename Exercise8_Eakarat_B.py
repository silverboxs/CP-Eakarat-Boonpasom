ram_price = 1280
cpu_price = 7880
totalPrice = 0

print("---->Welcome Silverbox Shop <----")
print(">>1. RAM DDR4 16Gb 2666MHz @ 1,280.-THB")
print(">>2. CPU intel Core i5 @ 7,880.-THB")
print("---------------------------------")
selectPD = input("Please select products 1 or 2 Enter.")
if selectPD == "1":
    print("Your choose >> RAM DDR4 16Gb 2666MHz")
    ea = int(input("Please enter the desired amount."))
    totalPrice = ram_price * ea
    print("Total : ",totalPrice,".-THB")
elif selectPD == "2":
    print("Your choose >> CPU intel Core i5")
    ea = int(input("Please enter the desired amount."))
    totalPrice = ram_price * ea
    print("Total : ",totalPrice,".-THB")
else:
    print("You have selected the wrong product.")
print("-------- Thank You --------")