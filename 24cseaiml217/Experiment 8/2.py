def square_of_number(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
print("The square of {number} is: ",square_of_number(number))