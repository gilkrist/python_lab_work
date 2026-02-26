# write a program to input 3 coefficent values and find the real roots
import math

print("For a quadratic equation in the form of ax^2 + bx + c = 0")
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Invalid input: 'a' cannot be zero for a quadratic equation.")
else:
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"The quadratic equation has two distinct real roots:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"The quadratic equation has one real (repeated) root:")
        print(f"Root: {root}")
    else:
        print("The quadratic equation has no real roots (the roots are complex).")

