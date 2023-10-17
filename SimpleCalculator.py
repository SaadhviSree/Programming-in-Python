'''
QUESTION:
Write a program in python using conditional statements to create a simple calculator

ALGORITHM : 
1) Start
2) Assign a variable answer to 0.
3) If the operator is + then store the sum of operands in answer.
4) If the operator is – then store the difference of operands in answer.
5) If the operator is * then store the product of operands in answer.
6) If the operator is / then store the quotient of the division in answer.
7) If none of the operators match print invalid operator.
8) Print the answer.
9) Stop
'''

operator=input("Enter the operator : ")
operand1=float(input("Enter a number : "))
operand2=float(input("Enter another number : "))
answer=0
if operator=="+": answer = operand1+operand2
elif operator=="-" : answer = operand1-operand2
elif operator=="/" : answer = operand1/operand2
elif operator=="*" : answer = operand1*operand2
else : print ("Invalid operator")
print("Answer :",answer)
