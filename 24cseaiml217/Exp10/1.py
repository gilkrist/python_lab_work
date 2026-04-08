""" 
WAP to create a class for employee having member data:empid,name,basic pay,ta,da,gross pay and member
function:disp(),calc(),use parameterised constructor to input the sample data.calc() to find ta=10% *basic pay,da=40%*basic pay
gross pay=basic pay +ta+da . disp() to display the information implement destructor
to releasing memory once use in over.Input an employee detailes and print.
"""
class Employee:
    def __init__(self, empid, name, basic_pay):
        self.empid = empid
        self.name = name
        self.basic_pay = basic_pay
        self.ta = 0
        self.da = 0
        self.gross_pay = 0
    def calc(self):
        self.ta = 0.1 * self.basic_pay
        self.da = 0.4 * self.basic_pay
        self.gross_pay = self.basic_pay + self.ta + self.da
    def disp(self):
        self.calc()   
        print(f"Employee ID: {self.empid}")
        print(f"Name: {self.name}")
        print(f"Basic Pay: {self.basic_pay}")
        print(f"TA: {self.ta}")
        print(f"DA: {self.da}")
        print(f"Gross Pay: {self.gross_pay}")
empid = input("Enter the employee id: ")
name = input("Enter the employee name: ")
basic_pay = float(input("Enter basic pay: "))
employee = Employee(empid, name, basic_pay)
employee.calc()
employee.disp()