# Wap to find a number is prime or not

number = int(input("Enter a number: "))

if number <= 1:
    print("not a prime number")
else:
    prime = False
    for i in range(2,int(number**0.5)+1):
        if number % i == 0:
            prime = True
            break

if not prime:
    print("It is a prime number")

else:
    print("It is not a prime number")