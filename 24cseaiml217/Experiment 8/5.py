def prime(number):
    if number <= 1:
        print("not a prime number")
    else:
        prime = False
        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                prime = True
                break

    if not prime:
        return "It is a prime number"

    else:
        return "It is not a prime number"

number = int(input("Enter a number: "))
print(prime(number))