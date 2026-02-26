# accept a digit within 0 to 6 like 0 is sunday and 1 is monday

num = int(input("enter a number between 0 to 6 to know which day it belongs to: "))

if num==0:
    print("Sunday-> Holly day")
elif num==1:
    print("Monday -> working day")
elif num==2:
    print("tuesday -> working day")
elif num==3:
    print("wednessday -> working day")
elif num==4:
    print("thursday -> working day")
elif num==5:
    print("friday -> working day")
elif num==6:
    print("saturday -> working day")

    