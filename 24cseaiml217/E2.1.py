#display simple interest and compound interest

p=int(input("Enter principal amount value = "));
r=int(input("Enter rate of interest value = "));
t=int(input("Enter time interval value = "));

si = (p*t*r)/100

print("The simple interest is = ", si);

ci=p*((1+r/100)**t)
print("the compund interest = ", ci)