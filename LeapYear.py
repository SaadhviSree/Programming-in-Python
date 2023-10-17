'''
QUESTION:
Write a program in python using conditional statements to check whether the given year is a leap year

ALGORITHM : 
1) Start
2) Input the year from the user.
3) Assign a variable leap to False.
4) Using if statement check if the year is divisible by 4 and not divisible by 100 or 
divisible by both 400 and 100.
5) If yes, then assign leap to True.
6) If leap is True print “is a leap year” else print “not a leap year”.
7) Stop
'''

year=int(input("Enter the year : "))
leap=False
if (year%4==0 and year%100!=0) or (year%400==0 and year%100==0): 
  leap=True
else : 
  leap=False
if leap : print(year,"is a leap year!!")
else : print(year,"is not a leap year.")
