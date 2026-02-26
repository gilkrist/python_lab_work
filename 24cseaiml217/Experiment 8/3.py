def square_of_number(number1, number2):
    return number1 + number2
number1, number2 = input("Enter a number: ").split()
number1 = int(number1)
number2 = int(number2)
print(f"The sum of {number1} and {number2} is: ",square_of_number(number1, number2))