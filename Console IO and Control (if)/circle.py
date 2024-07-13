#calculates the value of PI and then computes and displays
#the area of a circle with radius entered by the user
#Liyabona Mpapela
#6 August 2022
from math import sqrt 
pi = 2*(2/(sqrt(2))*(2/(sqrt(2+sqrt(2)))))*(2/(sqrt(2+sqrt(2+sqrt(2)))))
print("Approximation of pi: ",round(pi,4))
radius = eval(input("Enter the radius:\n"))
area = pi*radius*radius
print("Area:",round(area,4))
