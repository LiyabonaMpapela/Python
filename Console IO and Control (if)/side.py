#asks the user to enter the lengths 𝑎 and 𝑐, and calculates 𝑏
#correct to 4 decimal places
#Liyabona Mpapela
#6 August 2022
from math import*
a = eval(input("Enter the length of side a:\n"))
c = eval(input("Enter the length of side c:\n"))
b = sqrt((c*c)-(a*a))
if (a<0 or c<0):
    print("Sorry, lengths must be positive numbers.")
else:
    print("The length of side b is",round(b,4),end='.')
