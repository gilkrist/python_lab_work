# number is palendrom or no

number = int(input("Enter a number to check wether it is a palendrome number: "))
temporary = number
reverse = 0
while(number!=0):
    rem = number%10
    reverse = reverse * 10 + rem
    number = number//10

if reverse == temporary:
    print(f"{temporary} is a palindrome number")
else:
    print(f"{temporary} is not a palindrome number")
