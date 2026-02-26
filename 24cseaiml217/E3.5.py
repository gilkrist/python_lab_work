""" write a program to input marks for 5 subjects assume maximum marks for each subject is 50 find % and display as below 
% >= 90 and <= 100 grade is O
% >= 80 and <= 90 grade is E
% >= 70 and <= 80 grade is A
% >= 60 and <= 70 grade is B
% >= 50 and <= 60 grade is C
% >= 0 and <= 50 grade is F

"""

eng = int(input("enter english marks: "))
math = int(input("enter math marks: "))
sci = int(input("enter science marks: "))
soc = int(input("enter social marks: "))
his = int(input("enter history marks: "))

total_marks = eng + math + sci + soc + his

percentage = (total_marks/250)*100

if (percentage >=90 and percentage <= 100):
    print(f"you got O grade and scored {total_marks}")
elif (percentage >=80 and percentage <= 90):
    print(f"you got E grade and scored {total_marks}")
elif (percentage >=70 and percentage <= 80):
    print(f"you got A grade and scored {total_marks}")
elif (percentage >=60 and percentage <= 70):
    print(f"you got B grade and scored {total_marks}")
elif (percentage >=50 and percentage <= 60):
    print(f"you got C grade and scored {total_marks}")
elif (percentage >=0 and percentage <= 50):
    print(f"you got fail and scored {total_marks}")