'''
QUESTION:
Write a python program to calculate the roots of a quadratic equation

ALGORITHM : 
1) Start
2) Get the coefficients of each term in the equation.
3) Find the discriminant using the formula and store it.
4) Using the calculated discriminant find the roots of the quadratic equation using the 
quadratic formula. 
5) Print the calculated roots.
6) Stop
'''

a=int(input("Enter a : "))
b=int(input("Enter b : "))
c=int(input("Enter c : "))
d=((b**2)-4*a*c)**0.5
root1=(-b+d)/2*a
root2=(-b-d)/2*a
print("\nRoots are",root1,"and",root2)
