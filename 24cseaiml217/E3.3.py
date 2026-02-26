# find the greatest among 3 unequal numbers;
a,b,c=input("enter 3 numbers: ").split()

'''int(a)
int(b)
int(c)'''

print(f"the greatest among {a},{b} and {c} is ")

if(a>b and a>c): 
    print(f"{a} is the greatest")
elif (b>a and b>c):
    print(f"{b} is the greatest")
else:
    print(f"{c} is the greatest")