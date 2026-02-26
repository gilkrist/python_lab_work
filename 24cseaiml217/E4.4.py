# find the sum of the digit of the given interger

number = int(input("Enter a number: "))
temporary = number
sum = 0

for i in range(1, number+1):
    rem = number%10
    number = number//10
    sum += rem
print(f"The sum of the digits of the given number is: {sum}")