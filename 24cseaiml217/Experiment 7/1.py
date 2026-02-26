# WAP to create a list containing natural numbers from m to n where m and n given input (create useing for loop),find the sum, average ,
#  largest and smallest in the list. create another list which contains all the members of the first list except the numbers which is divisible by 3

start, end = input("Enter the start and end value of the lsit: ").split()
start = int(start)
end = int(end)
natural_numbers = []


for x in range(start, end):
    natural_numbers.append(x)

result_list = []
max = natural_numbers[0]
min = natural_numbers[0]
sum = 0

for x in natural_numbers:
    sum += x
    if x > max:
        max = x
    if x < min:
        min = x
    if x%3 != 0:
        result_list.append(x)

print(f"The sum of the list is {sum}, and the average of the list is {sum/len(natural_numbers)}")
print(f"The largest value is {max}, and the smallest value is {min}")
print(result_list)