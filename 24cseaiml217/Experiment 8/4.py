def square_of_number(number):
    factorial = 1
    while number >=1:
        factorial *= number
        number -= 1
    return factorial
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: ",square_of_number(number))