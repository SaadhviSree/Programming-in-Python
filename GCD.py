'''
QUESTION:
Write a python program to calculate GCD

ALGORITHM : 
1) Start
2) Input the first and second number from the user.
3) Assign the smaller number to a variable x.
4) Assign the value 1 to a variable GCD.
5) Iterating a for loop in range x with variable i, check if both x and y are divisible by i.
6) if yes then reassign a variable GCD to i.
7) Print GCD.
8) Stop
'''

x = int(input("Enter number 1 : "))
y = int(input("Enter number 2 : "))
count = 0
if x>y : count = x
else : count = y
gcd=1
for i in range(1,count) :
  if x%i==0 and y%i==0 : gcd = i
print("\nGCD is :",gcd)
