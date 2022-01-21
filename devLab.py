def customerDetail(name,year,sex):
    customerDB = list()
    age = 2017 - year
    customerDB.append(name)
    customerDB.append(age)
    customerDB.append(sex)
    return customerDB

#Input
ac = int(input())
CustomerList = list()

for rows in range(ac):
    n = input()
    y = int(input())
    s = input()
    db = customerDetail(n,y,s)
    CustomerList.append(db)

#Output
print("--Customers Information--")
for c in range(ac):
    print(CustomerList[c][0],"(age:",CustomerList[c][1],")")