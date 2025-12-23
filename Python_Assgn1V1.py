class electronicsMart:
    totalItems = 0
    print("               Inventory")
    print("*" * 40)
    print("Item Code", " ", "Item Quantity")
    def __init__(self,itemCode,itemName,itemQuantity,itemPrice):
        self.itemCode = itemCode
        self.itemName = itemName
        self.itemQuantity = itemQuantity
        self.itemPrice = itemPrice
    def inventory(self):
        print(self.itemCode, "", self.itemQuantity)
    print("*" * 40)

it1 = electronicsMart("101","Laptop",10,1000000)
it2 = electronicsMart("102","Cell Phone",20,20000)
it3 = electronicsMart("103","Speaker",25,10000)
it1.inventory()
it2.inventory()
it3.inventory()

from datetime import datetime

class Bill:
    def __init__(self, shop_name, tax_percent=5):
        self.shop_name = shop_name
        self.tax_percent = tax_percent
        self.items = []

    def add_item(self, name, price, qty):
        self.items.append((name, price, qty))

    def print_bill(self):
        subtotal = 0
        total_qty = 0

        print("\n" + self.shop_name.center(40, "-"))
        print("Date:", datetime.now().strftime("%d-%m-%Y %H:%M"))
        print("-" * 40)
        print("{:<15}{:<8}{:<8}{:<9}".format("Item", "Price", "Qty", "Total"))
        print("-" * 40)

        for name, price, qty in self.items:
            amount = price * qty
            subtotal += amount
            total_qty += qty
            print("{:<15}{:<8}{:<8}{:<9}".format(name, price, qty, amount))

        tax = subtotal * self.tax_percent / 100
        grand_total = subtotal + tax

        print("-" * 40)
        print(f"Total Quantity : {total_qty}")
        print(f"Subtotal      : ₹{subtotal}")
        print(f"Tax ({self.tax_percent}%)    : ₹{tax}")
        print(f"Grand Total   : ₹{grand_total}")
        print("-" * 40)
bill = Bill("ABC Mart", tax_percent=5)

bill.add_item("Laptop", 100000, 1)
bill.add_item("Cell Phone", 20000, 1)
bill.add_item("Speaker", 10000, 2)

bill.print_bill()


    #print("Total Items", electronicsMart.totalItems)

