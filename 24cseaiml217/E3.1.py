# write a program to test wether a string is palendrom or not
name = input("enter a name to check wether it is a palendrom or not: ")

if (name[::-1] == name):
    print(f"name: {name} is a palendrom")
else:
    print(f"name {name} is not a palendrom")