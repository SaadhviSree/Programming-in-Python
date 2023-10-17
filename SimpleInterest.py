'''
QUESTION:
Write a python program to calculate simple interest

ALGORITHM : 
1) Start
2) Get the input from the user for the values of principal amount,time duration and the 
rate of interest.
3) Using the formula si=ptr/100 frind the simple interest.
4) Print the calculated simple interest and amount(simple interst+pricipal amount).
5) Stop
'''

p=float(input("Enter the principal amount : "))
t=float(input("Enter the time duration : "))
r=float(input("Enter the rate of interest : "))
si=p*r*t/100
print("\nThe simple interest is",si)
print("The total amount is",p+si)
