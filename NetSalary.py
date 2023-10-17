'''
QUESTION:
Write a python program to calculate the net salary of an employee

ALGORITHM : 
1) Start
2) Get the basic salary, dearness allowance percentage, house rent allowance 
percentage, provident fund percentage and travel allowance percentage as input from the user.
3) Calculate the dearness allowance, house rent allowance, provident fund and travel allowance using the formula.
4) Calculate the gross salary by adding the basic salary with all the allowances. Now deduct the pf from gross salary to get the net salary. Print the net salary.
5) Stop
'''
 
bsal=float(input("Enter the basic salary : "))
DAP=float(input("Enter dearness allowance percentage : "))
DAsal=bsal*DAP/100
HRAP=float(input("Enter the house rent allowance percentage : "))
HRAsal=bsal*HRAP/100
PFP=float(input("Enter the provident fund percentage : "))
PFsal=bsal*PFP/100
TAP=float(input("Enter the travelling allowance percentage : "))
TAsal=TAP*bsal/100
