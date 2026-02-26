# generate fibonaci series between 0 to 1000 then find the sum of even value terms 

number = int(input("Enter a number: "))
sum = previous = 0
fibonacii = 1
for i in range(number):
    present = i
    fibonacii = previous + present
    print(fibonacii, end=", ")
    if fibonacii % 2 == 0:
        sum +=fibonacii
    previous = fibonacii

print("\n The sum of all the even fibonacci number is: ",sum)