#checking the validity of a time entered by the user as a set of
#three integers
#Liyabona Mpapela
#6 August 2022
hours = eval(input("Enter the hours:\n"))
minutes = eval(input("Enter the minutes:\n"))
seconds = eval(input("Enter the seconds:\n"))
if (hours < 0 or hours > 23) :
 print("Your time is invalid")
elif (minutes < 0 or hours > 60) :
 print("Your time is invalid")
elif (seconds < 0 or seconds > 60) :
 print("Your time is invalid.") 
else:
 print("Your time is valid.");
  
  
  
 