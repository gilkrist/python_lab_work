"""
wap to create a class product having member data:product id, product name,price,quantity,total ammount .
include member functions:
-calculate total() to calculate total ammount=price*quantity
-display() to display the product details
use parameterized constructor to input product details

"""
class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
        self.total_amount = 0

    def calculate_total(self):
        self.total_amount = self.price * self.quantity

    def display(self):
        self.calculate_total()
        print(f"Product ID: {self.product_id}")
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")
        print(f"Total Amount: {self.total_amount}")
product_id = input("Enter product id: ")
product_name = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
product = Product(product_id, product_name, price, quantity)
product.display()