'''
QUESTION:
Write a program in python using conditional statements to calculate grade of total mark

ALGORITHM : 
1) Start
2) Input the mark from the user.
3) Assign a variable grade to empty string.
9 | P a g e
4) Check is mark is between 0 to 100.
5) If mark greater than or equal to 91, grade is O.
6) If mark greater than or equal to 81, grade is A+.
7) If mark greater than or equal to 71, grade is A.
8) If mark greater than or equal to 61, grade is B+.
9) If mark greater than or equal to 51, grade is B.
10) If mark greater than or equal to 41, grade is P.
11) Else grade is RA.
12) Print the grade.
13) If mark is not between range then print mark is invalid.
14) Stop
'''

total=float(input("Enter the total mark : "))
grade=""
if total>=0 and total<=100:
    if total>=91 : grade = "O"
    elif total>=81 : grade = "A+"
    elif total>=71 : grade = "A"
    elif total>=61 : grade = "B+"
    elif total>=51 : grade = "B"
    elif total>=41 : grade = "P"
    else : grade = "RA"
    print("Grade :",grade)
else : print("Invalid mark")
