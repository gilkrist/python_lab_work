# find the factorial of a given number

temp = number = int(input("Enter a number: "))

factorial = 1

while number > 0:
    factorial *= number
    number -= 1
print(f"The factorial of {temp} is {factorial}")