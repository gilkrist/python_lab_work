"""
write a programe to create four base classes having individual methods addition(),substraction(),multiplication()
,divison() respectiviley ,craete a derived class for all above (multiple inheritance)having member data:data1,data2. create 
an object and then perform operations on the data1 and data2 
"""
class Addition:
    def addition(self):
        print("Addition:", self.data1 + self.data2)

class Subtraction:
    def subtraction(self):
        print("Subtraction:", self.data1 - self.data2)

class Multiplication:
    def multiplication(self):
        print("Multiplication:", self.data1 * self.data2)

class Division:
    def division(self):
        if self.data2 != 0:
            print("Division:", self.data1 / self.data2)
        else:
            print("Division: Cannot divide by zero")

class Calculator(Addition, Subtraction, Multiplication, Division):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

obj = Calculator(num1, num2)

obj.addition()
obj.subtraction()
obj.multiplication()
obj.division()