class Customer:
    name =""
    lastName = ""
    age = ""

    def addcart(self):
        print("Added to "+self.name+" "+self.lastName+"'s cart")

customer1 = Customer()
customer1.name = "Eakarat"
customer1.lastName = "Boonpasom"
customer1.age = 39
customer1.addcart()

customer2 = Customer()
customer2.name = "Sangwimol"
customer2.lastName = "Song"
customer2.age = 39
customer2.addcart()

customer3 = Customer()
customer3.name = "Panuwat"
customer3.lastName = "Boonpasom"
customer3.age = 38
customer3.addcart()